# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
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
            old_name='Phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='addresses',
            old_name='State',
            new_name='state',
        ),
    ]
