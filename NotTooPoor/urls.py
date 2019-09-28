
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from PoorUsers import views as UserViews


router = routers.DefaultRouter()
router.register(r'users', UserViews.CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(r'api-auth-token/', views.obtain_auth_token),

]
