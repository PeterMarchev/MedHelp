from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.translation import gettext_lazy as _


# Create your models here.
# I'm using "pillow" which is a library for working with images within python
# I can add other additional fields for info like bio and stuff in here


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name=_("imageprofile"))

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # to open the image for this profile instance and resize it
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
