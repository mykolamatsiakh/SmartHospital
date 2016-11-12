# coding=utf-8
from __future__ import unicode_literals
from django.db import models
import os


# Create your models here.
#from django.utils import six


class Hospital(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    home_page = models.CharField(max_length=250)
    time_from = models.TimeField(blank=True)
    time_to = models.TimeField(blank=True)
    image = models.ImageField(upload_to="media", default="media/image.jpg")
    def __unicode__(self):
        return self.title


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=100)
    speciality = models.CharField(max_length=100)
    bio = models.TextField()


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=100)




