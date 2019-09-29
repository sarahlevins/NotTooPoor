from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.conf import settings
from PoorEvents.models import Category

class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=50, default='', unique = True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    photo = models.ImageField(upload_to='uploads', blank=True)
    category = models.ManyToManyField('PoorEvents.Category', blank=True, default='')
    
    def __str__(self):
        return self.username
