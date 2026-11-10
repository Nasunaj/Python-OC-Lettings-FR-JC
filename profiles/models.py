"""
Data models for the profiles app.

Defines the Profile entity linked to a Django User.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represent a user profile.

    A profile is linked to exactly one Django User through
    a one-to-one relationship and stores a favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the username of the related user for display."""
        return self.user.username
