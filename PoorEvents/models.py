from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.conf import settings
from django.urls import reverse
from PoorUsers.models import CustomUser

class Event(models.Model):
    event_name = models.CharField(max_length=50, default='')
    event_description = models.CharField(max_length=500, default='')
    event_venue = models.ManyToManyField('Venue')
    event_start_datetime = models.DateTimeField('start time and date')
    event_end_datetime = models.DateTimeField('end time and date')
    event_photo = models.ImageField(upload_to = 'media/event_photos', null=True)
    host = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null = "True")

    # def get_absolute_url(self):
    #     return reverse("PoorEvents:event", kwargs={"pk": self.pk})

    def __str__(self):
        return self.event_name

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Venue(models.Model):
    venue_name = models.CharField(max_length=50, default='')
    venue_address = models.CharField(max_length=500, default='')
    venue_phone = models.FloatField(default ='0')
    venue_email = models.CharField(max_length=50, default='')
    venue_photo = models.ImageField(upload_to='media/venue_photos', null=True)
    
    def __str__(self):
        return self.venue_name