from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Hospital(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # image = models.ImageField()
    address = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    home_page = models.CharField(max_length=250)
    time_from = models.TimeField(blank=True)
    time_to = models.TimeField(blank=True)

    def __unicode__(self):
        return self.title
