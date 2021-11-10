import json
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

from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from gamelib.models import User
# first login
@csrf_exempt
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
        return JsonResponse({
            "message": "login failed",
            "status" : "failed", 
        })
    print('user : ' , user.full_name)
   # print('user : ' ,user)
    refresh = RefreshToken.for_user(user)
    # refresh = RefreshToken()

    return JsonResponse({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
  
@csrf_exempt
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



# Create your views here.
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
