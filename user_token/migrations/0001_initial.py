# Generated by Django 5.0.6 on 2024-07-03 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserToken",
            fields=[
                (
                    "token",
                    models.CharField(
                        auto_created=True,
                        max_length=16,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tokens",
                        to="user.user",
                    ),
                ),
            ],
        ),
    ]