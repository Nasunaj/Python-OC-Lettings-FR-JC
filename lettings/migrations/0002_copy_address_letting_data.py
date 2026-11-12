from django.db import migrations


def copy_address_and_letting_data(apps, schema_editor):
    """Copy data from the old oc_lettings_site tables to the new lettings tables."""
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    NewAddress = apps.get_model("lettings", "Address")
    OldLetting = apps.get_model("oc_lettings_site", "Letting")
    NewLetting = apps.get_model("lettings", "Letting")

    # Copie des adresses, en conservant les mêmes clés primaires
    # (indispensable pour que les Letting puissent pointer vers elles)
    for old_address in OldAddress.objects.all():
        NewAddress.objects.create(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )

    # Copie des locations, en conservant les mêmes id et address_id
    for old_letting in OldLetting.objects.all():
        NewLetting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address_id=old_letting.address_id,
        )


def reverse_copy_address_and_letting_data(apps, schema_editor):
    """Reverse migration: empty the new lettings tables."""
    NewLetting = apps.get_model("lettings", "Letting")
    NewAddress = apps.get_model("lettings", "Address")
    NewLetting.objects.all().delete()
    NewAddress.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),  # anciens modèles Address/Letting
    ]

    operations = [
        migrations.RunPython(
            copy_address_and_letting_data,
            reverse_copy_address_and_letting_data,
        ),
    ]
