from django.shortcuts import render
from rest_framework import viewsets
from PoorEvents.models import Event, Category, Venue, UserEventPreferences
from .serializers import EventSerializer, CategorySerializer, VenueSerializer, UserEventPreferencesSerializer
from django.views.generic import CreateView, UpdateView, DetailView, ListView


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventView(ListView):
    template_name = 'PoorEvents/index.html'
    queryset = Event.objects.all()
    context_object_name = 'events-list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class UserEventPreferencesViewSet(viewsets.ModelViewSet):
    queryset = UserEventPreferences.objects.all()
    serializer_class = UserEventPreferencesSerializer