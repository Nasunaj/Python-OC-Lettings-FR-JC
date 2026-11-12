"""
Views for the profiles app.

Render the list of profiles and the detail page of a single profile.
"""

from django.shortcuts import render

from .models import Profile


def index(request):
    """
    Render the profiles list page.

    Args:
        request: the HTTP request object.

    Returns:
        HttpResponse: the rendered profiles index template
        with all profiles in the context.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Render the detail page of a single profile.

    Args:
        request: the HTTP request object.
        username (str): the username of the user whose profile
        is displayed.

    Returns:
        HttpResponse: the rendered profile detail template
        with the profile in the context.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
