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


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['real_name', 'age', 'location',
                  'gender', 'disease', 'medications', 'about_user',
                  'doctor_qualifications', 'doctor_speciality', 'doctor_education', 'doctor_workspace', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        doctor_str = 'Only fill in if you are a doctor'
        self.fields['doctor_qualifications'].widget.attrs['placeholder'] = doctor_str
        self.fields['doctor_speciality'].widget.attrs['placeholder'] = doctor_str
        self.fields['doctor_education'].widget.attrs['placeholder'] = doctor_str
        self.fields['doctor_workspace'].widget.attrs['placeholder'] = doctor_str
