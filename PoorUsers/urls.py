from django.urls import path
import PoorUsers.views as views
from rest_framework import renderers

# user_list = CustomUserViewSet.as_view({
#     'get': 'list',
# })

# user_detail = CustomUserViewSet.as_view({
#     'get': 'retrieve',
# })

# urlpatterns = format_suffix_patterns([
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])

from django.urls import path

from . import views

app_name = 'PoorUsers'

urlpatterns = [
    # path('users/', user_list, name='user-list'),
    path('register/', views.CustomUserRegister.as_view(), name='register'),
    path('register_success/<int:pk>/', views.CustomUserRegisterSuccess.as_view(), name='register-success'),
    path('login/', views.CustomUserLogin.as_view(), name='login'),
    path('logout/', views.CustomUserLogout.as_view(), name='logout'),
    path('<int:pk>/', views.CustomUserDetail.as_view(), name='profile'),
    path('<int:pk>/update_account', views.EditCustomUserDetail.as_view(), name='update-account')
]