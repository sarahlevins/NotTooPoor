from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint allowing users to be viewed and editied
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class =  UserSerializer