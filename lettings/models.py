"""
Data models for the lettings app.

Defines the Address and Letting entities used to represent a property location
and its rental listing.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represent a physical address of a letting.

    Fields include street-level information, city, state, zip code and a
    3-character country ISO code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3,
                                        validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """Return the address as '{number} {street}' for display."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represent a letting (a rental property).

    A letting has a title and is linked to exactly one Address through a
    one-to-one relationship.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the letting title for display."""
        return self.title
