from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .forms import EditCustomUserForm, CreateCustomUserForm
from .models import CustomUser
from .serializers import CustomUserSerializer

"""
AUTHENTICATION
"""

class CustomUserRegister(CreateView):
    form_class = CreateCustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class CustomUserLogin(LoginView):
    template_name = 'registration/login.html'

class CustomUserLogout(LogoutView):
    next_page = reverse_lazy('PoorEvents:index')

"""
PROFILE VIEWS
"""

class CustomUserDetail(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'account.html'

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, pk=user_id)

class EditCustomUserDetail(LoginRequiredMixin, UpdateView):
    template_name = 'edit_user_account.html'
    form_class = EditCustomUserForm

    def get_success_url(self):
        user_id = self.kwargs['pk']
        return reverse_lazy('PoorUsers:profile', kwargs={'pk': user_id})

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, pk=user_id, username=self.request.user)

class PublicProfileDetail(LoginRequiredMixin, DetailView):
    model = CustomUser
    template = 'user_profile.html'

"""
VIEWSETS
"""

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(pk=user.id)


    
