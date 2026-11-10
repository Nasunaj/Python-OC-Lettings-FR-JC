"""
Admin configuration for the profiles app.

Registers the Profile model so it can be managed
from the Django admin site.
"""
from django.contrib import admin

from .models import Profile


admin.site.register(Profile)
