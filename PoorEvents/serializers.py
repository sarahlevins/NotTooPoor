from rest_framework import serializers
from PoorEvents.models import Category, Venue, Event, UserEventPreferences

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category'
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
    event_venue = VenueSerializer(read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    from PoorUsers.serializers import CustomUserSerializer
    host = CustomUserSerializer(read_only=True)    
    attendees = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'event_name',
            'event_description', 
            'event_venue', 
            'event_start_datetime',
            'event_end_datetime',
            'event_photo',
            'category',
            'host',
            'attendees',
            ]

class UserEventPreferencesSerializer(serializers.ModelSerializer):
    fav_category = CategorySerializer(many=True)
    fav_venues = VenueSerializer(many=True)
    fav_events = EventSerializer(many=True)

    class Meta:
        model = UserEventPreferences
        fields = [
            'user',
            'fav_category',
            'fav_venues',
            'fav_events'
        ]