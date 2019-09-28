from rest_framework import serializers
from .models import Event, Category, Venue

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'event_description', 
            'event_venue', 
            'event_start_datetime',
            'event_end_datetime',
            'event_photo',
            'host'
            ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category_name'
        ]

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = [
            'venue_name',
            'venue_address',
            'venue_phone',
            'venue_email',
            'venue_photo'
        ]
