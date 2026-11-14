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


def trigger_error(request):
    """
    Deliberately raise an exception to test Sentry integration.

    Temporary debug view: must be removed once Sentry is validated.

    Args:
        request: the HTTP request object.

    Raises:
        ZeroDivisionError: always, to test error reporting.
    """
    logger.error("Deliberate error triggered for Sentry testing")
    return 1 / 0
