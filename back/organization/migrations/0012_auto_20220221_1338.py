# Generated by Django 3.2.12 on 2022-02-21 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slack_bot", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("misc", "0004_auto_20210511_1242"),
        ("organization", "0011_alter_notification_notification_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="accent_color",
            field=models.CharField(
                default="#ffbb42", max_length=10, verbose_name="Accent color"
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="base_color",
            field=models.CharField(
                default="#99835C", max_length=10, verbose_name="Base color"
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="bot_color",
            field=models.CharField(
                default="#ffbb42", max_length=10, verbose_name="Bot color"
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="credentials_login",
            field=models.BooleanField(
                default=True,
                verbose_name="Allow users to login with their username and password",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="google_login",
            field=models.BooleanField(
                default=False,
                verbose_name="Allow users to login with their Google account",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="language",
            field=models.CharField(
                choices=[
                    ("en", "English"),
                    ("nl", "Dutch"),
                    ("fr", "French"),
                    ("de", "German"),
                    ("tr", "Turkish"),
                    ("pt", "Portuguese"),
                    ("es", "Spanish"),
                ],
                default="en",
                max_length=10,
                verbose_name="Language",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="logo",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="misc.file",
                verbose_name="Logo",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="name",
            field=models.CharField(max_length=500, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="organization",
            name="slack_confirm_person",
            field=models.ForeignKey(
                help_text="Slack only",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User to sent new hire account requests to",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="slack_default_channel",
            field=models.ForeignKey(
                help_text="Slack only",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="slack_bot.slackchannel",
                verbose_name="This is the default channel where the bot will post messages in",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="slack_login",
            field=models.BooleanField(
                default=False,
                verbose_name="Allow users to login with their Slack account",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="timezone",
            field=models.CharField(
                default="UTC", max_length=1000, verbose_name="Timezone"
            ),
        ),
        migrations.AlterField(
            model_name="welcomemessage",
            name="message",
            field=models.CharField(
                blank=True, max_length=20250, verbose_name="Message"
            ),
        ),
    ]
