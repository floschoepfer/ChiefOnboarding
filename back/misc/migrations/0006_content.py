# Generated by Django 3.2.12 on 2022-03-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("misc", "0005_delete_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
    ]