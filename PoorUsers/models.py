from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.conf import settings
from PoorEvents.models import Category

class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=50, default='', unique = True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='uploads', blank=True)
    category = models.ManyToManyField('PoorEvents.Category', blank=True, default='')

    def get_absolute_url(self):
        return reverse("PoorUsers:profile", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username
