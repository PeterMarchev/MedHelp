# Generated by Django 3.0.5 on 2020-06-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0011_auto_20200609_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
