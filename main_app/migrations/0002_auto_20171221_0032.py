# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 19:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addresses',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='addresses',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='addresses',
            old_name='Country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='addresses',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='addresses',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='addresses',
            old_name='State',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='addresses',
            name='Phone',
        ),
        migrations.AddField(
            model_name='addresses',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='contact_images'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='phone',
            field=models.IntegerField(default=123456789),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addresses',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]