"""
Unit and integration tests for the lettings app.

Covers the Address and Letting models, the views and the URL routes.
"""
import pytest

from django.urls import resolve, reverse
from lettings.models import Address, Letting
from lettings.views import index, letting


@pytest.fixture
def address():
    """Create and return a test Address at Madison Square Garden."""
    return Address.objects.create(
        number=4,
        street="Pennsylvania Plaza",
        city="New York",
        state="NY",
        zip_code=10001,
        country_iso_code="USA",
    )


@pytest.fixture
def letting_obj(address):
    """Create and return a test Letting near Madison Square Garden."""
    return Letting.objects.create(
        title="Courtside flat at Madison Square Garden",
        address=address,
    )


@pytest.mark.django_db
class TestAddress:
    """Test for the Address model."""

    def test_address_str_returns_number_and_street(self, address):
        """__str__ must return '{number} {street}'."""
        assert str(address) == "4 Pennsylvania Plaza"

    def test_address_creation(self, address):
        """An address is saved with the given values."""
        assert Address.objects.count() == 1
        assert address.city == "New York"


@pytest.mark.django_db
class TestLetting:
    """Tests for the Letting model."""

    def test_letting_str_returns_title(self, letting_obj):
        """__str__ must return the letting title."""
        assert str(letting_obj) == "Courtside flat at Madison Square Garden"

    def test_letting_is_linked_to_address(self, letting_obj, address):
        """The letting must be linked to the created address."""
        assert letting_obj.address == address


@pytest.mark.django_db
class TestLettingsViews:
    """Tests for the lettings views."""
    def test_index_returns_200_and_template(self, client, letting_obj):
        """The index view must return 200 and render the list template."""
        response = client.get(reverse("lettings:index"))
        assert response.status_code == 200
        assert 'lettings/index.html' in [t.name for t in response.templates]
        assert letting_obj in response.context['lettings_list']

    def test_letting_view_returns_200_and_context(self, client, letting_obj):
        """The detail view must return 200 with title and address."""
        response = client.get(
            reverse('lettings:letting', args=[letting_obj.id])
        )
        assert response.status_code == 200
        assert response.context['title'] == "Courtside flat at Madison Square Garden"
        assert response.context['address'] == letting_obj.address


class TestLettingsUrls:
    """Tests for the lettings URL routes (no DB needed)."""

    def test_index_url_resolves_to_index_view(self):
        """'/lettings/' must resolve to the lettings index view."""
        resolver = resolve('/lettings/')
        assert resolver.func == index

    def test_letting_url_resolves_to_letting_view(self):
        """'/lettings/<id>/' must resolve to the letting detail view."""
        resolver = resolve('/lettings/1/')
        assert resolver.func == letting
