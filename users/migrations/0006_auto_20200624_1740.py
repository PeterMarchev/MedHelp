# Generated by Django 3.0.5 on 2020-06-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_patient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='patient_name',
            field=models.CharField(default='', max_length=50, verbose_name='My name'),
        ),
    ]
