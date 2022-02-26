# Generated by Django 3.2.12 on 2022-02-21 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("admin_tasks", "0006_alter_admintask_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admintask",
            name="assigned_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Assigned to",
            ),
        ),
        migrations.AlterField(
            model_name="admintask",
            name="completed",
            field=models.BooleanField(default=False, verbose_name="Completed"),
        ),
        migrations.AlterField(
            model_name="admintask",
            name="date",
            field=models.DateField(blank=True, null=True, verbose_name="Date"),
        ),
        migrations.AlterField(
            model_name="admintask",
            name="email",
            field=models.EmailField(
                blank=True, default="", max_length=12500, verbose_name="Email"
            ),
        ),
        migrations.AlterField(
            model_name="admintask",
            name="name",
            field=models.CharField(max_length=500, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="admintask",
            name="new_hire",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="new_hire_tasks",
                to=settings.AUTH_USER_MODEL,
                verbose_name="New hire",
            ),
        ),
        migrations.AlterField(
            model_name="admintask",
            name="option",
            field=models.IntegerField(
                choices=[(0, "No"), (1, "Email"), (2, "Slack")],
                verbose_name="Send email or text to extra user?",
            ),
        ),
        migrations.AlterField(
            model_name="admintask",
            name="priority",
            field=models.IntegerField(
                choices=[(1, "Low"), (2, "Medium"), (3, "High")],
                default=2,
                verbose_name="Priority",
            ),
        ),
        migrations.AlterField(
            model_name="admintask",
            name="slack_user",
            field=models.CharField(
                blank=True, default="", max_length=12500, verbose_name="Slack user"
            ),
        ),
    ]
