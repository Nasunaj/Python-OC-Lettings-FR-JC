"""
Views for the oc_lettings_site project.

Contains the home page view of the site.
"""
import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the home page of the site.

    Args:
        request: the HTTP request object.

    Returns:
        HttpResponse: the rendered home page template.
    """
    logger.info("Rendering the home page")
    return render(request, 'index.html')
