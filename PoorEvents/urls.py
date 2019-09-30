from django.urls import path
from PoorEvents.views import IndexView, EventListView, EventCreateView, EventDetailView, VenueDetailView
from rest_framework import renderers


app_name = 'PoorEvents'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('event_create/', EventCreateView.as_view(), name='event-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('venues/<slug:slug>/', VenueDetailView.as_view(), name='venue-detail'),
    ]


