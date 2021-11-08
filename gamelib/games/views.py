# views.py
from json.encoder import JSONEncoder
from django.db.models import query
from django.http.response import JsonResponse
from rest_framework import response, serializers, viewsets

from .serializers import GameSerializer,RequirementSerializer
from gamelib.models import Game, Rating, Requirement
from rest_framework import generics,filters



# game = Game.objects.get(pk=1)
# categories = game.categories.all()
# print(game.name + "" )
# for i in range(len(categories)):
#     print(categories[i].name)
# from django_filters.rest_framework import DjangoFilterBackend
# class GameList(generics.ListAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['categories']
import django_filters
class GameFilter(django_filters.FilterSet):
    ids = django_filters.Filter(field_name='categories',lookup_expr='in')
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name','release_date']
    class Meta:
        model = Game
        fields = ('id','name')
class GameFilterCategory(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_class = GameFilter
    
class GameFilterOrderByName(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name','release_date']
class GameSearchName(generics.ListCreateAPIView):
    search_fields = ['name','publisher']
    filter_backends = (filters.SearchFilter,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.filter(pk=4)
    serializer_class = GameSerializer
class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.filter(pk=1)
    serializer_class = RequirementSerializer
class GameLatest(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('-release_date')[:5]
    serializer_class = GameSerializer
class GamePopular(viewsets.ModelViewSet) :
    
    popular_games = Rating.objects.raw("SELECT  1 as id , game_id_id , (SELECT SUM(s) FROM UNNEST(rate) s) as total_usage from gamelib_rating ")
    print("len : " , len(popular_games))
    print(type(popular_games))
    games_id = []
    rates = []
    games_dict = {}
    for i in range(len(popular_games)) :
        games_id.append(popular_games[i].game_id_id) 
        rates.append(popular_games[i].total_usage/5)
    print('game : ' , games_id) 
    print('rate',rates)
    for i in range(len(games_id)):
        break_points = 0
        
        if i == len(games_id) - 1 or games_id[i] != games_id[i+1]:
            break_points = i + 1
            games_dict[games_id[i]] = sum(rates[:break_points])/len(rates[:break_points])
            rates = rates[break_points:]
            
    print(games_dict)
    data = {}
    gameess=[]
    count = 1 
    for key in games_dict.keys() :
        if games_dict[key] > 5.0 :
            gameess.append(key)
            
    #queryset 
    print(type(gameess) , type(gameess[0])) 
    
    queryset = Game.objects.filter(id__in=gameess)
    serializer_class = GameSerializer
    # def retrieve(self, request, *args, **kwargs):
    #     # ret = super(StoryViewSet, self).retrieve(request)
    #     return response.Response({'key': 'single value' , 'data': 1})

    # def list(self, request, *args, **kwargs):
    #     # ret = super(StoryViewSet, self).list(request)
    #     return response.Response({'key': 'list value' , 'data' : JsonResponse(self.queryset , safe=False)})
    #queryset = gameess
    # print(type(gameess))
    # data["message"] = "get popular game with rating > 5.0"
    # data["status"] = "true"

    # data["data"] = gameess
    
    # return JsonResponse(data , safe=False)
