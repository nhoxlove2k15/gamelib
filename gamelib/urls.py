
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
# get game popular,latest
router = routers.DefaultRouter()
router.register(r'games/popular' , GamePopular)
router.register(r'games/latest' , GameLatest)
router.register(r'games', GameViewSet)

# urlconf
urlpatterns = [
    path('', include(router.urls)),
    # get game by sort , search , filter 
    path('game/tag/', GameSearchByCategory.as_view()),
    path('game/ordered/',GameSortByNameAndDate.as_view()),
    path('game/', GameSearchByName.as_view()),
    path('game/filter/',GameFilterByDate.as_view()),
    
    path('users', user_list),
    
    # create rating , comment
    path('users/rating/<int:user_id>', create_rating),
    path('users/comment/<int:user_id>',create_comment),
    path('users/comments',get_comment),

    # create like , delete like , get like by id
    path('users/like/<int:user_id>' , get_create_delete_like),
    #path('users/like/<int:user_id>' , show_like_list),

    # details game
    path('game/detail/<int:game_id>' , get_detail_game),
    # authen user
    path('users/hello' , say_hello),
    path('users/login' , get_tokens_for_user),
    path('users/register', create_user),
    
    
    
]