"""
Unit and integration tests for the oc_lettings_site project.

Covers the home page view, the root URL routes and the 404 error page.
"""
import pytest

from django.urls import resolve

from oc_lettings_site.views import index


@pytest.mark.django_db
class TestHomeView:
    """Tests for the home page view."""

    def test_index_returns_200_and_template(self, client):
        """The home view must return 200 and render the index template."""
        response = client.get('/')
        assert response.status_code == 200
        assert 'index.html' in [t.name for t in response.templates]


class TestRootUrls:
    """Tests for the root URL routes (no DB needed)."""

    def test_root_url_resolves_to_index_view(self):
        """'/' must resolve to the home view."""
        resolver = resolve('/')
        assert resolver.func == index

    def test_lettings_urls_are_namespaced(self):
        """'/lettings/' must be routed by the lettings app."""
        resolver = resolve('/lettings/')
        assert resolver.view_name == 'lettings:index'

    def test_profiles_urls_are_namespaced(self):
        """'/profiles/' must be routed by the profiles app."""
        resolver = resolve('/profiles/')
        assert resolver.view_name == 'profiles:index'


@pytest.mark.django_db
class TestErrorPages:
    """Tests for the custom error pages."""

    def test_unknown_url_returns_404(self, client):
        """An unknown URL must return a 404 status code."""
        response = client.get('/this-page-does-not-exist/')
        assert response.status_code == 404
