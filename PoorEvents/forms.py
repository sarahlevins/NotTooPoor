from django import forms
from django.forms import ModelForm, DateTimeInput
from django.contrib.admin import widgets

from .models import Event

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
        'event_name', 
        'event_description', 
        'event_venue',
        'event_start_datetime',
        'event_end_datetime', 
        'category',)
