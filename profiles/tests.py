"""
Unit and integration tests for the profiles app.

Covers the Profile model, the views and the URL routes.
"""
import pytest

from django.contrib.auth.models import User
from django.urls import resolve, reverse

from profiles.models import Profile
from profiles.views import index, profile


@pytest.fixture
def user():
    """Create and return a test User."""
    return User.objects.create_user(
        username="knicksfan",
        password="Knicks2026",
    )


@pytest.fixture
def profile_obj(user):
    """Create and return a test Profile linked to the user fixture."""
    return Profile.objects.create(
        user=user,
        favorite_city="New York",
    )


@pytest.mark.django_db
class TestProfile:
    """Tests for the Profile model."""

    def test_profile_str_returns_username(self, profile_obj):
        """__str__ must return the related user's username."""
        assert str(profile_obj) == "knicksfan"

    def test_profile_creation(self, profile_obj):
        """A profile is saved with the given values."""
        assert Profile.objects.count() == 1
        assert profile_obj.favorite_city == "New York"

    def test_profile_is_linked_to_user(self, profile_obj, user):
        """The profile must be linked to the created user."""
        assert profile_obj.user == user


@pytest.mark.django_db
class TestProfilesViews:
    """Tests for the profiles views."""

    def test_index_returns_200_and_template(self, client, profile_obj):
        """The index view must return 200 and render the list template."""
        response = client.get(reverse('profiles:index'))
        assert response.status_code == 200
        assert 'profiles/index.html' in [t.name for t in response.templates]
        assert profile_obj in response.context['profiles_list']

    def test_profile_view_returns_200_and_context(self, client, profile_obj):
        """The detail view must return 200 with the profile in context."""
        response = client.get(
            reverse('profiles:profile', args=[profile_obj.user.username])
        )
        assert response.status_code == 200
        assert response.context['profile'] == profile_obj


class TestProfilesUrls:
    """Tests for the profiles URL routes (no DB needed)."""

    def test_index_url_resolves_to_index_view(self):
        """'/profiles/' must resolve to the profiles index view."""
        resolver = resolve('/profiles/')
        assert resolver.func == index

    def test_profile_url_resolves_to_profile_view(self):
        """'/profiles/<username>/' must resolve to the profile detail view."""
        resolver = resolve('/profiles/knicksfan/')
        assert resolver.func == profile
