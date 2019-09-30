from django.urls import path
from PoorEvents.views import EventViewSet, EventView, CategoryViewSet, VenueViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns


event_list = EventViewSet.as_view({
    'get': 'list',
})

event_detail = EventViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = format_suffix_patterns([
    path('', event_list, name='event-list'),
    path('events/<int:pk>/', event_detail, name='user-detail')
])

