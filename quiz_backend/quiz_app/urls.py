from django.urls  import path
from .serializers import *
from .views       import *

urlpatterns = [
    # API-DJANGO
    # accounts
    path('accounts/api/login/',  login  ),
    path('accounts/api/logout/', log_out),
    # Quiz
    path('api/quizzes/',       QuizList  ),
    path('api/quiz/<int:pk>/', QuizDetail),
    # User
    path('api/users/',         userList  ),
    path('api/user/<int:pk>/', userDetail),
    # Score
    path('api/scores/',         ScoreList  ),
    path('api/score/<int:pk>/', ScoreDetail),
    # Player
    path('api/players/',         PlayerList  ),
    path('api/player/<int:pk>/', PlayerDetail),
    # Category
    path('api/categories/',        categoryList  ),
    path('api/category/<int:pk>/', categoryDetail),
    # Archive
    path('api/archive/', ArchiveList),
]