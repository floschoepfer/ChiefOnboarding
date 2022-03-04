# Generated by Django 3.2.8 on 2021-11-09 03:07

from django.db import migrations, models

from misc.migration_scripts.content_migrations import (
    RunPythonWithArguments,
    migrate_wysiwyg_field,
)


class Migration(migrations.Migration):

    dependencies = [
        ("to_do", "0003_auto_20201013_0149"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="content_json",
            field=models.JSONField(
                default="[]", verbose_name=models.TextField(default="[]")
            ),
            preserve_default=False,
        ),
        RunPythonWithArguments(
            migrate_wysiwyg_field, context={"app": "to_do", "model": "todo"}
        ),
    ]
