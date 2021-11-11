
from django.conf.urls import include
from django.urls import path
from gamelib.views import *
from django.urls import  path
from rest_framework import routers
from gamelib.games.views import *
from gamelib.users.views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter()
router.register(r'games/popular' , GamePopular)
router.register(r'games/latest' , GameLatest)
router.register(r'games', GameViewSet)

# urlconf
urlpatterns = [
    path('', include(router.urls)),
    path('game/tag/', GameFilterCategory.as_view()),
    path('game/ordered/',GameFilterOrderByName.as_view()),
    path('game/', GameSearchName.as_view()),
    path('game/filter/',FF.as_view()),
    
    path('game/rating/', create_rating),
    
    path('hello' , say_hello),
    path('token' , get_tokens_for_user),
    path('register', create_user),
    path('game/popular' , get_game_popular),
    #path('game/latest' , get_game_latest),
    
    
]