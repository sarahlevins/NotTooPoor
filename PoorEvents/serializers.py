from rest_framework import serializers
from .models import Event, Category, Venue
from PoorUsers.serializers import CustomUserSerializer


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
            'venue_streetnum',
            'venue_street',
            'venue_suburb',
            'venue_postcode',
            'venue_website',
            'venue_email',
            'venue_photo'
        ]


class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)
    host = CustomUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            'event_name',
            'event_description', 
            'venue', 
            'event_start_datetime',
            'event_end_datetime',
            'event_photo',
            'host',
            'category',
            ]

