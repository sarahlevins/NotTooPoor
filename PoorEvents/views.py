from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView
from django.shortcuts import render
from rest_framework import viewsets

from PoorEvents.models import Event, Category, Venue, UserEventPreferences
from .forms import NewEventForm
from .serializers import EventSerializer, CategorySerializer, VenueSerializer, UserEventPreferencesSerializer


class IndexView(TemplateView):
    template_name = 'index.html'

class EventListView(ListView):
    template_name = 'event_list.html'
    queryset = Event.objects.order_by('-event_start_datetime')
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.all()

class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = 'event_create.html'
    form_class = NewEventForm

    def form_valid(self, form):
        form.instance.host = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'


class VenueDetailView(DetailView):
    model = Venue
    template_name = 'venue_detail.html'
    context_object_name = 'venue'

"""
VIEWSETS
"""

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