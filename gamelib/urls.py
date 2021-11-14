
from django.conf.urls import include
from django.urls import path
from gamelib.views import *
from django.urls import  path
from rest_framework import routers
from gamelib.games.views import *
from gamelib.users.views import *
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# get game popular,latest
# router = routers.DefaultRouter()
# router.register(r'games/popular' , GamePopular)
# router.register(r'games/latest' , GameLatest)
# router.register(r'games', GameViewSet)

# urlconf
urlpatterns = [
    #path('', include(router.urls)),
    path('games/popular',GamePopular.as_view()),
    path('games/latest',GameLatest.as_view()),

    # get game by sort , search , filter 
    path('games/tag/', GameSearchByCategory.as_view()),
    path('games/ordered/',GameSortByNameAndDate.as_view()),
    path('games/search', GameSearchByName.as_view()),
    path('games/filter/',GameFilterByDate.as_view()),
    # details game
    path('games/detail/<int:game_id>' , GameDetailEngine.as_view()),

    #path('users', user_list),
    
    # create rating , comment
    path('users/rating/<int:user_id>', RatingEngine.as_view()),
    path('users/comment/<int:user_id>',CommentEngine.as_view()),
   # path('users/comments',get_comment),

    # create like , delete like , get like by id
    path('users/like/<int:user_id>' , LikeEngine.as_view()),
    #path('users/like/<int:user_id>' , show_like_list),

    
    # authen user
    #path('users/hello' , say_hello),
    path('users/login' , UserLoginEngine.as_view()),
    path('users/register', UserRegisterEngine.as_view()),

    # path('openapi/', get_schema_view(
    #     title="School Service",
    #     description="API developers hpoing to use our service"
    # ), name='openapi-schema'),

    # path('docs/', TemplateView.as_view(
    #     template_name='documentation.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
    
    
]