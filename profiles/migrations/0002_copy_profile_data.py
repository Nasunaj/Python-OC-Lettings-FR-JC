from django.db import migrations


def copy_profile_data(apps, schema_editor):
    """Copy profiles from oc_lettings_site to the new profiles app."""
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=old_profile.id,
            favorite_city=old_profile.favorite_city,
            user_id=old_profile.user_id,
        )


def reverse_copy_profile_data(apps, schema_editor):
    """Reverse migration: empty the new profiles table."""
    NewProfile = apps.get_model("profiles", "Profile")
    NewProfile.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),  # ancien modèle Profile
    ]

    operations = [
        migrations.RunPython(copy_profile_data, reverse_copy_profile_data),
    ]