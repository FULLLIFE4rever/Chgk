from django.urls import include, path
from rest_framework import routers

from .views import QuestionAddViewSet, QuestionViewSet

app = "api"

router = routers.DefaultRouter()
router.register("add", QuestionAddViewSet, basename="add")
router.register("question", QuestionViewSet, basename="question")

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("", include(router.urls)),
]
