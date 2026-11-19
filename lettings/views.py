"""
Views for the lettings app.

Render the list of lettings and the detail page of a single letting.
"""
import logging

from django.http import Http404
from django.shortcuts import render

from lettings.models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the lettings list page.

    Args:
        request: the HTTP request object.

    Returns:
        HttpResponse: the rendered lettings index template with all lettings
        in the context.
    """
    logger.info("Rendering lettings list page")
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Render the detail page of a single letting.

    Args:
        request: the HTTP request object.
        letting_id (int): the primary key of the letting to display.

    Returns:
        HttpResponse: the rendered letting detail template with the letting
        title and address in the context.
    Raises:
        Http404: if no letting exists with the given letting id.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.warning("Letting not found: id=%s", letting_id)
        raise Http404
    logger.info("Rendering letting detail: id=%s", letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
