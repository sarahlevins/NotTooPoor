from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from .models import CustomUser, UserProfile
from .serializers import CustomUserSerializer, UserProfileSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(pk=user.id)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



    
