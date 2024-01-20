# Generated by Django 5.0.1 on 2024-01-15 18:56

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionuser",
            name="create",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 16, 21, 56, 54, 465960)
            ),
        ),
        migrations.AlterField(
            model_name="questionuser",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]