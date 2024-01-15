from questions.models import Championship, Question
from .serializers import ChampionshipSerializer, NameSerializer
from rest_framework.viewsets import ModelViewSet


class ChampionshipViewSet(ModelViewSet):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer


class NameViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = NameSerializer
    permission_classes = ()
