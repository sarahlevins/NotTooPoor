from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.conf import settings

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, default='', unique = True)
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    photo = models.ImageField(upload_to='uploads', blank=True)
    phone = models.IntegerField(default='0')