from django.contrib import admin
from PoorEvents.models import Event, Category, Venue, UserEventPreferences

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Venue)
admin.site.register(UserEventPreferences)
