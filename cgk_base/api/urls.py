from django.urls import path, include
from rest_framework import routers
from .views import ChampionshipViewSet, QuestionViewSet

app = 'api'

router = routers.DefaultRouter()
router.register('championship', ChampionshipViewSet, basename='Championship')
router.register('questions', QuestionViewSet, basename='Questions')

urlpatterns = [
    path("", include(router.urls)),
]
