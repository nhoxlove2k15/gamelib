import json
from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
import hashlib
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.generics import(ListAPIView, ListCreateAPIView)
import datetime
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from gamelib.models import  *
from gamelib.serializers import  CommentSerializer, GetLikeSerializer, LikeSerializer, RatingSearializer, UserLoginSerializer, UserRegisterSerializer, UserSerializer

class UserLoginEngine(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        #serializer = CommentSerializer(data=self.request.data)
        try:
            username = body['user_name']
            password = body['pass_word']
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
            users = User.objects.filter(user_name = username , pass_word = hashlib.md5(password.encode()).hexdigest() )
        except ObjectDoesNotExist:
            users = None
        if users is None : 
            return Response({
                "message": "login failed",
                "status" : "failed", 
            })
        print('user : ' , users)
    # print('user : ' ,user)
        #refresh = RefreshToken.for_user(user)
        # refresh = RefreshToken()
        serializer = UserSerializer(users , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

    # def post(self, request, *args, **kwargs):
    #     serializer = UserLoginSerializer()
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)    
    #     return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
class UserRegisterEngine(generics.GenericAPIView): 
    serializer_class = UserRegisterSerializer
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['user_name']
        password = body['pass_word']
        fullname = body['full_name']
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
class CommentEngine(generics.GenericAPIView): 
    
    serializer_class = CommentSerializer
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
class RatingEngine(generics.GenericAPIView):    
    serializer_class = RatingSearializer
    def post(self, request, *args, **kwargs):
        serializer = RatingSearializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    def put(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        game_id = body["game_id"]
        user_id = body["user_id"]
        rate = Rating.objects.get(user_id=user_id ,game_id=game_id)
        serializer = RatingSearializer(rate,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeEngine(generics.ListCreateAPIView): 
    serializer_class = LikeSerializer
    def get(self,request,*args,**kwargs):
        number = request.path[request.path.rfind('/') + 1: ]
        print("hello:" , number )
        # try :
        likes = Like.objects.filter(user_id = int(number))
        # catch:
        #     likes = None
        serializer = GetLikeSerializer(likes, many=True)
        if likes.exists() == False : 
            return JsonResponse({
                "message": "user chua like game nao or ko co user nay`",
                "status" : 0 , 
                "data" : serializer.data
            })
        else :
            return JsonResponse({
                "message": "user co like ",
                "status" : 1, 
                "data" : serializer.data
            })
    def post(self, request, *args, **kwargs):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                print(e.__class__, e.__cause__)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def delete(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        game_id = body["game_id"]
        user_id = body["user_id"]
        like = Like.objects.get(user_id=user_id,game_id=game_id)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  


    
