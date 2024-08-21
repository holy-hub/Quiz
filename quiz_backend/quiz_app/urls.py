from rest_framework.routers import DefaultRouter

from django.urls  import path, include
from .views import *

routers = DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'categories', CategoryViewSet)
routers.register(r'quizzes', QuizViewSet)
routers.register(r'players', PlayerViewSet)
routers.register(r'scores', ScoreViewSet)

# API-DJANGO
urlpatterns = [
    path('', include(routers.urls)),
]