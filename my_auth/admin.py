from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm
from .models import CustomUser, ThumbnailSize, UserTier


# Register your models here.

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = (
        'username',
        'email',
        'is_staff',
        'is_superuser',
        'tier'
    )
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('User Tier', {'fields': ('tier',)}),
        ('Permissions', {
            'fields': (
                'is_staff',
                'is_active',
                'is_superuser',
                'user_permissions')
                }
        ),
        ('Additional stats', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Username', {'fields': ('username',)}),
        ('User Tier', {'fields': ('tier',)}),
    )


admin.site.register(UserTier)