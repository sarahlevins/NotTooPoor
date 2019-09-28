from django.urls import path
from PoorEvents.views import EventViewSet, CategoryViewSet, VenueViewSet
from rest_framework import renderers

event_list = EventViewSet.as_view({
    'get': 'list',
})

event_detail = EventViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = format_suffix_patterns([
    path('events/', event_list, name='event-list'),
    path('events/<int:pk>/', event_detail, name='user-detail')
])