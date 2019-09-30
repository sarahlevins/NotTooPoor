from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """
    fields that show when editing a user
    """
    fieldsets = (
        (None, {'fields': (
            'username',
            'first_name',
            'last_name',
            'dob',
            'email',  
            'password', 
            'category',
            )}),
        (('Permissions'), {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    """
    fields that show when creating a user
    """
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                                'username',
                'first_name',
                'last_name',
                'dob',
                'email',  
                'password1', 
                'password2',
                'category',
                ),
        }),
    )
    list_display = ('username','email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    