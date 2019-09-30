from django.urls import path
import PoorEvents.views as views
from rest_framework import renderers

app_name = 'PoorEvents'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('events/', views.EventView.as_view(), name='event-list')
    ]


