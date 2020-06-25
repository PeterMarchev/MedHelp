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
    patient_name = models.CharField(max_length=50, default = "", verbose_name=_("My name"))
    age = models.CharField(max_length=3, default = _("N/A"), verbose_name=_("Age"))
    location = models.CharField(max_length=50, default = _("N/A"),  verbose_name=_("Location"))
    about_user = models.TextField(default = _("N/A"), verbose_name=_("About me"))
    disease = models.CharField(max_length=100, default = _("N/A"),  verbose_name=_("Diseases"))
    medications = models.CharField(max_length=100, default = _("N/A"),  verbose_name=_("Medications"))
    GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('N/A', 'Not Specified'),
]
    gender = models.CharField(max_length=6, default = _("N/A"),  choices=GENDER_CHOICES)
    doctor_qualifications = models.CharField(max_length=50, default = "",  verbose_name=_("Qualification"))
    doctor_speciality = models.CharField(max_length=50, default = "",  verbose_name=_("Speciality"))
    doctor_education = models.CharField(max_length=50, default = "",  verbose_name=_("University"))
    doctor_workspace = models.CharField(max_length=50, default = "",  verbose_name=_("Workplace"))


    @property
    def is_doctor(self):
        return self.user.groups.filter(name="Doctors").exists()

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
