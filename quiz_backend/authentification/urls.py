from django.urls import path
from .views import *

urlpatterns = [
    # accounts
    path('accounts/api/login/',  login_user),
    path('accounts/api/logout/', login_user),
]
