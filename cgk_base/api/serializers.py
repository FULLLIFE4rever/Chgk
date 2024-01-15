from rest_framework import serializers
from questions.models import Championship, Question, Name


class QuestionReadSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('question',
                  'handout',
                  'answer',
                  'images_and_audio',
                  'rating')

    def get_rating(self, instanse):
        _correct_ans = instanse.correct_answers
        _all_answers = instanse.incorrect_answers + instanse.correct_answers
        if _all_answers:
            return (_correct_ans << 2) / _all_answers
        return 'Нет ответов'


class NameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Name
        fields = ('first_name',
                  'last_name')


class ChampionshipSerializer(serializers.ModelSerializer):
    questions = QuestionReadSerializer(many=True)
    author = NameSerializer()
    championship_url = serializers.SerializerMethodField()

    class Meta:
        model = Championship
        fields = ('__all__')

    def get_championship_url(self, obj):
        pass
