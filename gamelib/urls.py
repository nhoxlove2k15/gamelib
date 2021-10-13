from django.conf.urls import url
from django.urls import path
from gamelib.models import User 
from gamelib.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# urlconf
urlpatterns = [
    path('hello' , say_hello),
    path('token' , get_tokens_for_user),
    path('register', create_user),
    
]