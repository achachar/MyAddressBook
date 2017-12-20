# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-19 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_addresses_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresses',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='contact_images'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='phone',
            field=models.IntegerField(),
        ),
    ]