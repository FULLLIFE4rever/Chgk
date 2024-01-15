# Generated by Django 5.0.1 on 2024-01-12 15:32

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.TextField(max_length=100)),
                ("last_name", models.TextField(max_length=100)),
                ("city", models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Championship",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        db_index=True,
                        help_text="Поле должно состоять из букв латинского алфавита и цифр",
                        max_length=8,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^([0-9a-fA-F]{,8})$",
                                message="Поле заполнено не верно!",
                            )
                        ],
                        verbose_name="Сокрщенное название чемпионата",
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        max_length=150, verbose_name="Название чемпионата"
                    ),
                ),
                ("date", models.DateField(verbose_name="Дата игры")),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="championship_author",
                        to="questions.author",
                        verbose_name="Автор чемпионата",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField(max_length=3500, verbose_name="Вопрос")),
                ("answer", models.TextField(max_length=1500, verbose_name="Ответ")),
                (
                    "handout",
                    models.TextField(
                        blank=True, max_length=3500, null=True, verbose_name="Раздатка"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        max_length=4500,
                        null=True,
                        verbose_name="Коментарий",
                    ),
                ),
                (
                    "images_and_audio",
                    models.TextField(verbose_name="Фотографии и аудио"),
                ),
                (
                    "correct_answers",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Правельные ответы"
                    ),
                ),
                (
                    "incorrect_answers",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Неправельные ответы"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="question_author",
                        to="questions.author",
                        verbose_name="Автор вопроса",
                    ),
                ),
                (
                    "questions",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_championship",
                        to="questions.championship",
                        verbose_name="Вопрос чемпионта",
                    ),
                ),
            ],
        ),
    ]
