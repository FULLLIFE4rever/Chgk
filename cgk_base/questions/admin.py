from django.contrib import admin

from .models import Question, QuestionUser

# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "question",
        "answer",
        "handout",
        "comment",
        "images",
        "audio",
        "correct_answers",
        "incorrect_answers",
    )
    search_fields = (
        "answer",
        "question",
    )
    list_filter = (
        "answer",
        "question",
    )
    list_editable = ("question", "answer", "handout", "comment")


@admin.register(QuestionUser)
class QuestionUserAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "user",
        "create",
    )
    search_fields = ("create",)
    list_filter = ("create",)
