from django.db import models
from rest_framework import serializers
from .models import CustomUser, UserProfile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name'
        ]

class UserProfileSerializer(serializers.ModelSerializer):
    favourite_categories = serializers.ManyToManyField('PoorEvents.CategorySerializer', read_only=True)
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'dob',
            'photo',
            'phone',
            'favourite_categories',
        ]



