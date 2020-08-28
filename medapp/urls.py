from django.urls import path
from .views import(
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentDeleteView
)
from . import views


urlpatterns = [
    path('', views.home, name='medapp-home'),
    # was "path('forum/', views.forum, name='medapp-forum')"
    path('forum/', PostListView.as_view(), name='medapp-forum'),
    # grabbing PK value from URL and using it in the view function (im using class based view so thats where its going to pass it )
    # TODO: i might use this to view specific user profiles later
    path('forum/post/<int:pk>/', views.post_detail,
         name='post-detail'),  # 'post/<int:pk>/' .... PostDetailView.as_view()
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('forum/post/new', PostCreateView.as_view(), name='post-create'),

    path('forum/post/<int:pk>/update/',
         PostUpdateView.as_view(), name='post-update'),

    path('forum/post/<int:pk>/delete/',
         PostDeleteView.as_view(), name='post-delete'),

    path('forum/post/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path('about/', views.about, name='medapp-about'),  # view was about
    path('dermatologists/', views.find_derm, name='medapp-test'),
    path('neurologists/', views.find_neur, name='medapp-test'),
    path('orthopedists/', views.find_orth, name='medapp-test'),
    path('pediatricians/', views.find_pedi, name='medapp-test'),
    path('oncologists/', views.find_onco, name='medapp-test'),
    path('forum/announcements/', views.announcement, name='announcement'),
    




]
