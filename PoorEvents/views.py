from django.shortcuts import render
from rest_framework import viewsets
from PoorEvents.models import Event, Category, Venue, UserEventPreferences
from .serializers import EventSerializer, CategorySerializer, VenueSerializer, UserEventPreferencesSerializer
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class EventView(ListView):
    template_name = 'event_list.html'
    queryset = Event.objects.all()

    def get_queryset(self):
        return Event.objects.all()

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class UserEventPreferencesViewSet(viewsets.ModelViewSet):
    queryset = UserEventPreferences.objects.all()
    serializer_class = UserEventPreferencesSerializer