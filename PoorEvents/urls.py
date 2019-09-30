from django.urls import path
import PoorEvents.views as views
from rest_framework import renderers

app_name = 'PoorEvents'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('events/', views.EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('venues/<slug:slug>/', views.VenueDetailView.as_view(), name='venue-detail'),
    ]


