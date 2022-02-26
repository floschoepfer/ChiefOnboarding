# Generated by Django 3.2.12 on 2022-02-21 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("to_do", "0017_auto_20220209_0122"),
        ("misc", "0004_auto_20210511_1242"),
        ("sequences", "0014_auto_20220113_2208"),
    ]

    operations = [
        migrations.AlterField(
            model_name="condition",
            name="condition_to_do",
            field=models.ManyToManyField(
                related_name="condition_to_do",
                to="to_do.ToDo",
                verbose_name="Trigger after these to do items have been completed:",
            ),
        ),
        migrations.AlterField(
            model_name="condition",
            name="condition_type",
            field=models.IntegerField(
                choices=[
                    (0, "After new hire has started"),
                    (1, "Based on one or more to do item(s)"),
                    (2, "Before the new hire has started"),
                    (3, "Without trigger"),
                ],
                default=0,
                verbose_name="Block type",
            ),
        ),
        migrations.AlterField(
            model_name="condition",
            name="days",
            field=models.IntegerField(
                default=0,
                verbose_name="Amount of days before/after new hire has started",
            ),
        ),
        migrations.AlterField(
            model_name="condition",
            name="time",
            field=models.TimeField(default="08:00", verbose_name="At"),
        ),
        migrations.AlterField(
            model_name="externalmessage",
            name="content",
            field=models.CharField(
                blank=True, max_length=12000, verbose_name="Content"
            ),
        ),
        migrations.AlterField(
            model_name="externalmessage",
            name="content_json",
            field=models.ManyToManyField(to="misc.Content", verbose_name="Content"),
        ),
        migrations.AlterField(
            model_name="externalmessage",
            name="name",
            field=models.CharField(max_length=240, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="externalmessage",
            name="person_type",
            field=models.IntegerField(
                choices=[(0, "New hire"), (1, "Manager"), (2, "Buddy"), (3, "custom")],
                default=1,
                verbose_name="Person type",
            ),
        ),
        migrations.AlterField(
            model_name="externalmessage",
            name="send_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Send to",
            ),
        ),
        migrations.AlterField(
            model_name="externalmessage",
            name="send_via",
            field=models.IntegerField(
                choices=[(0, "Email"), (1, "Slack"), (2, "Text")],
                verbose_name="Send via",
            ),
        ),
        migrations.AlterField(
            model_name="externalmessage",
            name="subject",
            field=models.CharField(
                blank=True,
                default="Here is an update!",
                max_length=78,
                verbose_name="Subject",
            ),
        ),
        migrations.AlterField(
            model_name="pendingadmintask",
            name="assigned_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assigned_user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Assigned to",
            ),
        ),
        migrations.AlterField(
            model_name="pendingadmintask",
            name="comment",
            field=models.CharField(
                blank=True, default="", max_length=12500, verbose_name="Comment"
            ),
        ),
        migrations.AlterField(
            model_name="pendingadmintask",
            name="date",
            field=models.DateField(blank=True, null=True, verbose_name="Due date"),
        ),
        migrations.AlterField(
            model_name="pendingadmintask",
            name="email",
            field=models.EmailField(
                blank=True, default="", max_length=12500, verbose_name="Email"
            ),
        ),
        migrations.AlterField(
            model_name="pendingadmintask",
            name="name",
            field=models.CharField(max_length=500, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="pendingadmintask",
            name="option",
            field=models.CharField(
                choices=[(0, "No"), (1, "Email"), (2, "Slack")],
                max_length=12500,
                verbose_name="Option",
            ),
        ),
        migrations.AlterField(
            model_name="pendingadmintask",
            name="priority",
            field=models.IntegerField(
                choices=[(1, "Low"), (2, "Medium"), (3, "High")],
                default=2,
                verbose_name="Priority",
            ),
        ),
        migrations.AlterField(
            model_name="pendingadmintask",
            name="slack_user",
            field=models.CharField(
                blank=True, default="", max_length=12500, verbose_name="Slack option"
            ),
        ),
        migrations.AlterField(
            model_name="sequence",
            name="name",
            field=models.CharField(max_length=240, verbose_name="Name"),
        ),
    ]
