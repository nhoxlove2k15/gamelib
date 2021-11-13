import json
from os import name
from django.http.response import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
import hashlib
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpRequest,HttpResponse
from rest_framework.response import Response
from rest_framework.generics import(ListAPIView, ListCreateAPIView)
import datetime

from rest_framework import serializers, status
from rest_framework.settings import api_settings
from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from gamelib.models import Comment, Game, Like, User
# # first login
# @csrf_exempt
# def get_tokens_for_user(request):
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#     try:
#         username = body['username']
#         password = body['password']
#     except ObjectDoesNotExist:  
#         username = None
#         password = None
    
#     print("authen : " , username + " " + password )
#     if username is None or password is None :
#         return JsonResponse({
#             "message": "login failed",
#             "status" : "failed", 
#         })
#     try:
#         user = User.objects.get(user_name = username , pass_word = hashlib.md5(password.encode()).hexdigest() )
#     except ObjectDoesNotExist:
#         user = None
#     if user is None : 
#         return JsonResponse({
#             "message": "login failed",
#             "status" : "failed", 
#         })
#     print('user : ' , user.full_name)
#    # print('user : ' ,user)
#     refresh = RefreshToken.for_user(user)
#     # refresh = RefreshToken()

#     return JsonResponse({
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     })
  
# @csrf_exempt
# def create_user(request):
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#     username = body['username']
#     password = body['password']
#     fullname = body['fullname']
#     user = User.objects.create(full_name=fullname , user_name = username , pass_word = hashlib.md5(password.encode()).hexdigest() , created_at = datetime.datetime.now())
#     if user == None:
#         return JsonResponse({
#             "message": "login failed",
#             "status" : "failed", 
#         })
#     return JsonResponse({
#             "message": "register successfully",
#             "status" : "true", 
#         })



# # Create your views here.
# @csrf_exempt
# def say_hello(request):
#     body = request.headers
#     #body = json.loads(body_unicode)
#     token = body["Authorization"][7:]
#     print("token: " + token)
#     if token is None :
#         data = {
#             'message' : 'false',
#             'status' : 200
#         }
#     else :
#         data = {
#             'message' : 'true',
#             'status' : 200
#         }

#     return JsonResponse(data)
  
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from gamelib.models import Rating, User
from gamelib.serializers import  CommentSerializer, GetCommentSerializer, GetGameDetailSerializer, GetGameSerializer, GetLikeSerializer, LikeSerializer, RatingSearializer, UserSerializer

@api_view(['GET'])
def get_comment(request):  
    comments = Comment.objects.all()
    serializer = GetCommentSerializer(comments,many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def show_like_list(request,user_id):
    pass
@api_view(['GET','POST','DELETE'])
def get_create_delete_like(request,user_id):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    game_id = body["game_id"]
    if request.method == 'GET':
        likes = Like.objects.all().filter(user_id = user_id)
        serializer = GetLikeSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                print(e.__class__, e.__cause__)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        like = Like.objects.get(user_id=user_id,game_id=game_id)
        like.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

def detail_game():
    pass         
@api_view(['GET'])
def get_detail_game(request,game_id):
    game = Game.objects.filter(pk=game_id)
    serializer_game = GetGameSerializer(game , many=True)
    comments = Comment.objects.filter(game_id=game_id)
    serializer_comment = GetCommentSerializer(comments,many=True)
    rates = Rating.objects.filter(game_id=game_id)
    serializer_rate = RatingSearializer(rates,many=True)
    #print(type(serializer_rate.data))
    a = serializer_rate.data
    # zipped_lists= zip(a[i]['rate'] for i in range(len(a)))
    # list1 = [1, 2, 3]
    # list2 = [4, 5, 6]

    # zipped_lists = zip(list1, list2)
    # print(zipped_lists)
    # sum_ = [x + y for (x, y) in zipped_lists]
    # print(sum_)
    b = []
    for i in range(len(a)):
        b.append(a[i]['rate'])
    v = [sum(x) for x in zip(*b)]
    print(v)
    return JsonResponse({
        'game' : serializer_game.data,
        'comment':serializer_comment.data,
        'rate' : {
            'story':v[0],
            'gameplay':v[1],
            'sound':v[2],
            'graphic':v[3],
            'overall':v[4]
        }
    })
@api_view(['POST'])
def create_comment(request,user_id):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    game_id = body["game_id"]
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            print(e.__class__, e.__cause__)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['POST','PUT'])
def create_rating(request,user_id):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    game_id = body["game_id"]
    if request.method == 'POST':    
        serializer = RatingSearializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                print(e.__class__, e.__cause__)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        rate = Rating.objects.get(user_id=user_id ,game_id=game_id)
        serializer = RatingSearializer(rate,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_list(request):
    # List all user, or create new user
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                print(e.__class__, e.__cause__)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# frist login
@api_view(['GET'])
def get_tokens_for_user(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    try:
        username = body['username']
        password = body['password']
    except ObjectDoesNotExist:  
        username = None
        password = None
    
    print("authen : " , username + " " + password )
    if username is None or password is None :
        return JsonResponse({
            "message": "login failed",
            "status" : "failed", 
        })
    try:
        user = User.objects.get(user_name = username , pass_word = hashlib.md5(password.encode()).hexdigest() )
    except ObjectDoesNotExist:
        user = None
    if user is None : 
        return Response({
            "message": "login failed",
            "status" : "failed", 
        })
    print('user : ' , user.full_name)
   # print('user : ' ,user)
    refresh = RefreshToken.for_user(user)
    # refresh = RefreshToken()

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
 # sign up 
@api_view(['POST'])
def create_user(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    fullname = body['fullname']
    user = User.objects.create(full_name=fullname , user_name = username , pass_word = hashlib.md5(password.encode()).hexdigest() , created_at = datetime.datetime.now())
    if user == None:
        return JsonResponse({
            "message": "login failed",
            "status" : "failed", 
        })
    return JsonResponse({
            "message": "register successfully",
            "status" : "true", 
        })

# get  user data
#@api_view(['GET'])
@csrf_exempt
def say_hello(request):
    body = request.headers
    #body = json.loads(body_unicode)
    token = body["Authorization"][7:]
    print("token: " + token)
    if token is None :
        data = {
            'message' : 'false',
            'status' : 200
        }
    else :
        data = {
            'message' : 'true',
            'status' : 200
        }

    return JsonResponse(data)
# @APIView(['GET', 'PUT', 'DELETE', 'PATCH'])
# def user_detail(request, pk):
#     #Retrieve, update or delete a user
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PATCH':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
  