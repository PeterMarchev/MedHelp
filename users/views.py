from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # hashes password and saves user
            #username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created successfully! You can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
    #by passing parameters in, i'm also populating form with the current info
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
        request.FILES,
        instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Update successful')
            return redirect('profile')



    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
  

    #passing to template by creating a context (which is a dictionery with its keys being the variables we will access within the template)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'users/profile.html', context) #passing context here so we can access the forms
