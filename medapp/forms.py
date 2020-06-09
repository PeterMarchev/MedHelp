from .models import Comment, Post
from users.models import Profile
from django import forms
from django.utils.translation import gettext as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [_('body')]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        return super().save(*args, **kwargs)