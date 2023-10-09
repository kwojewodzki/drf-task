from django.contrib import admin
from .models import User, ThumbnailSize, UserTier

# Register your models here.

admin.site.register(User)
admin.site.register(ThumbnailSize)
admin.site.register(UserTier)
