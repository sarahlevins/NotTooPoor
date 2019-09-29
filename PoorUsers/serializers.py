from django.db import models
from rest_framework import serializers
from .models import CustomUser, UserProfile


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email', 
        ]

class UserProfileSerializer(serializers.ModelSerializer):
    from PoorEvents.serializers import CategorySerializer
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'user',
            'dob',
            'photo',
            'category',
        ]



