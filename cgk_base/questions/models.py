import datetime as dt

from django.contrib.auth import get_user_model
from django.db import models

from .validators import validate_is_audio

User = get_user_model()


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

    images = models.ImageField(
        blank=True, null=True, verbose_name="Фотографии", upload_to="images/"
    )
    audio = models.FileField(
        blank=True,
        null=True,
        verbose_name="Аудио",
        upload_to="audio/",
        validators=(validate_is_audio,),
    )
    correct_answers = models.PositiveIntegerField(
        verbose_name="Правельные ответы", default=0
    )
    incorrect_answers = models.PositiveIntegerField(
        verbose_name="Неправельные ответы", default=0
    )


class QuestionUser(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="question_user",
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="question_user",
        primary_key=True,
    )
    create = models.DateTimeField(
        default=dt.datetime.now() + dt.timedelta(days=1)
    )
