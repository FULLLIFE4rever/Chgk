from rest_framework import serializers

from questions.models import Question, QuestionUser


class QuestionAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("question", "handout", "answer", "images", "audio")


class QuestionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("question", "handout", "images", "audio")


class UserAnswerSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ("pk", "comment", "answer", "rating", "question")
        read_only_fields = ("pk", "comment", "rating", "question")

    def get_rating(self, instanse):
        _correct_ans = instanse.correct_answers
        _all_answers = instanse.incorrect_answers + instanse.correct_answers
        if _all_answers:
            return (_correct_ans << 2) / _all_answers
        return "Нет ответов"


class QuestionUserSerializer(serializers.ModelSerializer):
    question = QuestionReadSerializer(read_only=True)

    class Meta:
        model = QuestionUser
        fields = ("question",)
