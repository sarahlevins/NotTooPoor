
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from PoorUsers import views as UserViews
from PoorEvents import views as EventViews 


router = routers.DefaultRouter()
router.register(r'users', UserViews.CustomUserViewSet)
router.register(r'events', EventViews.EventViewSet)
router.register(r'venues', EventViews.VenueViewSet)
router.register(r'categories', EventViews.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(r'api-auth-token/', views.obtain_auth_token),

]
