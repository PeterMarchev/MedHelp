from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from users.models import Profile
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Comment
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def post_detail(request, pk):
    template_name = 'medapp/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST, user=request.user)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm(user=request.user)
        print("Hello", comment_form)

    context = {
        'user': request.user,
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request,  template_name, context)


def about(request):  # about test page
    return render(request, 'medapp/about.html')


def home(request):  # landing page blog
    from django.utils import translation

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    if request.method == 'POST':
        message_content = request.POST['message-content']
        message_title = request.POST['message-title']
        message_sender = request.POST['message-email']
        made_by = """Author: """

        send_mail(
            message_title,
            made_by + message_sender + """
        
Message: """ + message_content,
            message_sender,
            ['petardm.uni@gmail.com'],
            fail_silently=False
        )

        return render(request, 'medapp/index.html', {'message_sender': message_sender})

    else:

        return render(request, 'medapp/index.html')


def forum(request):  # forum page about
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'medapp/forum.html', context)

# PostListView replaces the forum/ view in urls.py
# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-display/


class PostListView(ListView):
    model = Post
    template_name = 'medapp/forum.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # orders posts from latest to oldest
    paginate_by = 5


class UserPostListView(ListView):  # in order to get all posts by said user
    model = Post
    template_name = 'medapp/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # filters posts by said user and orders them from latest to oldest
        viewed_user = User.objects.get(username=user)
        return Post.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(
            User, username=self.kwargs.get('username'))
        return context


class PostDetailView(DetailView):
    model = Post

    # def get(self, request, *args, **kwargs):
    #   post = get_object_or_404(Post, pk=kwargs['pk'])
    #  template_name = 'medapp/post_detail.html'
    #  comments = Comment.objects.filter(post=post).values()
    #  print("hello")
    #  return render(request, template_name, {'post': post, 'comments': comments})

    # def post_detail(self, request):
    #   model = Post
    #   template_name = 'post_detail.html'
    #   print("working")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # setting author for new post
        return super().form_valid(form)

# using LoginRequiredMixin so people can't create posts if they aren't logged in
# using UserPassesTestMixin so people can't edit the posts of other users than themselves


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()  # gets post we're trying to update
        if self.request.user == post.author:  # checks if the person trying to edit is the author himself
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/forum/'

    def test_func(self):
        post = self.get_object()  # gets post we're trying to update
        if self.request.user == post.author:  # checks if the person trying to edit is the author himself
            return True
        return False
