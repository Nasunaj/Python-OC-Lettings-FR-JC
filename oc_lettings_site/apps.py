"""
Application configuration for the oc_lettings_site app.

The root app only serves the home page of the site.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """Configuration class of the oc_lettings_site application."""
    name = 'oc_lettings_site'
