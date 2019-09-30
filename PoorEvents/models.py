from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.conf import settings
from django.urls import reverse

class Event(models.Model):
    event_name = models.CharField(max_length=50, default='')
    event_description = models.CharField(max_length=500, default='')
    event_venue = models.ForeignKey('Venue', on_delete=models.DO_NOTHING, default='')
    event_start_datetime = models.DateTimeField('start time and date')
    event_end_datetime = models.DateTimeField('end time and date')
    event_photo = models.ImageField(upload_to ='media/event_photos', blank=True)
    host = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default='')
    category = models.ManyToManyField('Category', default='')
    attendees = models.ManyToManyField('PoorUsers.CustomUser', related_name='attendees', default='')

    def get_absolute_url(self):
        return reverse("PoorEvents:event", kwargs={"pk": self.pk})

    def __str__(self):
        return self.event_name

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Venue(models.Model):
    venue_name = models.CharField(max_length=50, default='')
    venue_streetnum = models.IntegerField(default=0, blank=True)
    venue_street = models.CharField(max_length=50, default='')
    venue_suburb = models.CharField(max_length=50, default='')
    venue_postcode = models.IntegerField(default='')
    venue_website = models.URLField(max_length=100, default='')
    venue_email = models.CharField(max_length=50, default='')
    venue_photo = models.ImageField(upload_to='media/venue_photos', blank=True)
    
    def __str__(self):
        return self.venue_name

class UserEventPreferences(models.Model):
    user = models.OneToOneField('PoorUsers.CustomUser', on_delete=models.CASCADE, related_name='userpreferences', default='')
    fav_category = models.ManyToManyField('Category', default='')
    fav_venues = models.ManyToManyField('Venue', default='')
    fav_events = models.ManyToManyField('Event', default='')

    def __str__(self):
        return self.user.username