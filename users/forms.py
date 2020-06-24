from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.utils.translation import gettext as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'password1': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1']:
            self.fields[fieldname].help_text = None


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', ]


# inherits from ModelForm. Allows us to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  # model we want to work with is Profile
        # fields that we want to work with (in our case just image)
        fields = ['patient_name', 'age', 'location', 'gender', 'about_user', 'disease', 'medications', 'image']
