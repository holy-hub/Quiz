from django.urls    import path
from .serializers   import *
from .views         import *

urlpatterns = [
    # API-DJANGO
    # accounts
    path('accounts/api/login/',  login,   name='login' ),
    path('accounts/api/logout/', log_out, name='logout'),
    # Quiz
    path('api/quizzes/',       QuizList,   name='QuizList'  ),
    path('api/quiz/<int:pk>/', QuizDetail, name='QuizDetail'),
    # Score
    path('api/scores/',         ScoreList,   name='ScoreList'  ),
    path('api/score/<int:pk>/', ScoreDetail, name='ScoreDetail'),
    # User
    path('api/users/',         userList,   name='categoryList'  ),
    path('api/user/<int:pk>/', userDetail, name='categoryDetail'),
    # Category
    path('api/categories/',        categoryList,   name='categoryList'  ),
    path('api/category/<int:pk>/', categoryDetail, name='categoryDetail'),
]
