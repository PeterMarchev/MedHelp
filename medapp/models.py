from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
# Each class is a different table in the db.
# Each attribute is different field in the db.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"))
    date_posted = models.DateTimeField(default=timezone.now)
    # Takes author name from the authors table. If user is deleted, all his posts are deleted too
    # each post can only have 1 author. Author is FK for User
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='authors')
    objects = models.Manager()  # for an error msg i had

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # returning path to a specific post
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(verbose_name=_("body"))
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)

    def save(self):  # overwriting save method from the parent class
        super().save()
