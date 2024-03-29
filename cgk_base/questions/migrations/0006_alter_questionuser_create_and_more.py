# Generated by Django 5.0.1 on 2024-01-17 21:08

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "questions",
            "0005_alter_question_audio_alter_question_images_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionuser",
            name="create",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 19, 0, 8, 36, 806372)
            ),
        ),
        migrations.AlterField(
            model_name="questionuser",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="questions.question",
            ),
        ),
    ]
