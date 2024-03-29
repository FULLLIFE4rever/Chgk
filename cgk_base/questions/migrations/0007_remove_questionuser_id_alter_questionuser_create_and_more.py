# Generated by Django 5.0.1 on 2024-01-18 14:34

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0006_alter_questionuser_create_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="questionuser",
            name="id",
        ),
        migrations.AlterField(
            model_name="questionuser",
            name="create",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 19, 17, 34, 17, 942174)
            ),
        ),
        migrations.AlterField(
            model_name="questionuser",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
