"""
Views for the oc_lettings_site project.

Contains the home page view of the site.
"""

from django.shortcuts import render


def index(request):
    """
    Render the home page of the site.

    Args:
        request: the HTTP request object.

    Returns:
        HttpResponse: the rendered home page template.
    """
    return render(request, 'index.html')
