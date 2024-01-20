import datetime as dt

from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
)
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from questions.models import Question, QuestionUser

from .serializers import (
    QuestionAddSerializer,
    QuestionUserSerializer,
    UserAnswerSerializer,
)

User = get_user_model()


class QuestionAddViewSet(
    CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet
):
    queryset = Question.objects.all()
    serializer_class = QuestionAddSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()


class QuestionViewSet(ModelViewSet):
    queryset = QuestionUser.objects.all()
    serializer_class = QuestionUserSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        return QuestionUser.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        question = Question.objects.all().order_by("?")[0]
        create = dt.datetime.now() + dt.timedelta(days=1)
        try:
            get_questuser = QuestionUser.objects.get(user=user)
            get_questuser.question = question
            get_questuser.create = create
        except QuestionUser.DoesNotExist:
            get_questuser = QuestionUser.objects.create(
                user=user, question=question, create=create
            )
        get_questuser.save()
        # serializer = QuestionUserSerializer(data=data)
        # serializer.is_valid()

    @action(
        detail=False,
        methods=["post"],
        permission_classes=(IsAuthenticated,),
        serializer_class=UserAnswerSerializer,
    )
    def answer(self, request):
        answer = request.data["answer"]
        user = request.user
        obj = QuestionUser
        return self._get_answer(obj, user, answer)

    def _get_answer(self, obj, user, answer):
        user = user
        try:
            question_user = obj.objects.get(user=user)
        except QuestionUser.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
        question = question_user.question
        data = {"answer": answer}
        serializer = self.get_serializer(question, data=data)
        serializer.is_valid(raise_exception=True)
        if answer == question.answer:
            question.correct_answers += 1
        else:
            question.incorrect_answers += 1
        question.save()
        question_user.delete()
        return Response(serializer.data, status=HTTP_200_OK)
