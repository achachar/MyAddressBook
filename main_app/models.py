# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Addresses(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    image = models.ImageField(upload_to='contact_images', default='media/default.jpg')

    def __str__(self):
        return self.name
