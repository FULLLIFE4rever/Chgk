from django.db import models
from django.core.validators import RegexValidator
from users.models import Name, User
from datetime import datetime
from django.conf import settings


class Championship(models.Model):
    """Championship model"""

    foreign_url = models.URLField(
        max_length=40, null=True, blank=True, default=settings.URL_CONFIG
    )
    slug = models.CharField(
        max_length=8,
        db_index=True,
        help_text="Поле должно состоять из 8 букв латинского алфавита или цифр",
        unique=True,
        validators=[
            RegexValidator(
                "^([0-9a-fA-F]{,8})$",
                message=("Поле заполнено не верно!"),
            )
        ],
        verbose_name="Сокрщенное название чемпионата",
    )
    name = models.TextField(
        max_length=150, verbose_name="Название чемпионата"
    )
    author = models.ForeignKey(
        Name,
        null=True,
        related_name="championship_author",
        verbose_name="Автор чемпионата",
        on_delete=models.SET_NULL,
    )
    date = models.DateField(
        "Дата добавления игры", auto_now_add=True, null=True
    )


class Question(models.Model):
    """Question model"""

    question = models.TextField(max_length=3500, verbose_name="Вопрос")
    answer = models.TextField(max_length=1500, verbose_name="Ответ")
    handout = models.TextField(
        max_length=3500, blank=True, null=True, verbose_name="Раздатка"
    )
    comment = models.TextField(
        max_length=4500, blank=True, null=True, verbose_name="Коментарий"
    )
    author = models.ForeignKey(
        Name,
        null=True,
        db_index=True,
        related_name="author",
        verbose_name="Автор вопроса",
        on_delete=models.SET_NULL,
    )
    images_and_audio = models.TextField(verbose_name="Фотографии и аудио")
    correct_answers = models.PositiveIntegerField(
        verbose_name="Правельные ответы", default=0
    )
    incorrect_answers = models.PositiveIntegerField(
        verbose_name="Неправельные ответы", default=0
    )
    championship = models.ForeignKey(
        Championship,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Вопрос чемпионта",
        related_name="question",
    )


class QuestionUser(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(
        default=datetime.now() + datetime.time(day=1), auto_now_add=True
    )
