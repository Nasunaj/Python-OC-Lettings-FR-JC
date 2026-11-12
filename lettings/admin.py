"""
Admin configuration for the lettings app.

Registers the Address and Letting models so they can be
managed from the Django admin site.
"""

from django.contrib import admin

from .models import Address, Letting

admin.site.register(Address)
admin.site.register(Letting)
