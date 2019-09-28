from django.urls import path
from PoorUsers.views import CustomUserViewSet
from rest_framework import renderers

user_list = CustomUserViewSet.as_view({
    'get': 'list',
})

user_detail = CustomUserViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = format_suffix_patterns([
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
