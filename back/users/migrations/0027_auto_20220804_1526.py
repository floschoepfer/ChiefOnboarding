# Generated by Django 3.2.13 on 2022-08-04 15:26

from django.db import migrations
from django.utils.crypto import get_random_string


class Migration(migrations.Migration):
    def rotate_unique_url_for_demo_user(apps, schema_editor):
        User = apps.get_model("users", "User")
        while True:
            unique_string = get_random_string(length=8)
            if not User.objects.filter(unique_url=unique_string).exists():
                break
        # There can only be one, but just to make sure it still exists we use filter
        User.objects.filter(unique_url="SIyuR6pG").update(unique_url=unique_string)

    dependencies = [
        ("users", "0026_alter_user_timezone"),
    ]

    operations = [
        migrations.RunPython(rotate_unique_url_for_demo_user),
    ]