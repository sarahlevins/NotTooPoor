
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from rest_framework import routers
from rest_framework.authtoken import views

import PoorEvents

from PoorUsers import views as UserViews
from PoorEvents import views as EventViews 


router = routers.DefaultRouter()
router.register(r'users', UserViews.CustomUserViewSet)
router.register(r'events', EventViews.EventViewSet)
router.register(r'venues', EventViews.VenueViewSet)
router.register(r'categories', EventViews.CategoryViewSet)
router.register(r'userpreferences', EventViews.UserEventPreferencesViewSet)

urlpatterns = [
    path('', include('PoorEvents.urls')),
    path('users/', include('PoorUsers.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(r'api-auth-token/', views.obtain_auth_token),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
