# Generated by Django 5.0 on 2023-12-08 06:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("bio", models.TextField(blank=True)),
                (
                    "profileimg",
                    models.ImageField(
                        default="blank-profile-pic.png", upload_to="profile_images"
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
