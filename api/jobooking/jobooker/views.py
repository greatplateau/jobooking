from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from jobooker.models import Jobooker
from jobooker.serializer import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .tools import *
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SigninForm
from oauth2_provider.models import Application
from oauth2_provider.decorators import protected_resource 


@api_view(['POST'])
def create_jobooker(request):
    serialized = UserSerializer(data=request.DATA)
   
    if serialized.is_valid():
       
        User.objects.create_user(
           
 
           serialized.data['username'],
            serialized.data['email'],
            serialized.data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def sign_in(request):
    serialized = UserSerializer(data=request.DATA)
    username = serialized.initial_data['username']
    password = serialized.initial_data['password']
    print username + " " + password
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
	    #login(request,user)
            Application.objects.filter(user_id = user.id).delete()
            Application.objects.create(user=user,name="jobooker", 
                                   client_type=Application.CLIENT_CONFIDENTIAL,
                                   authorization_grant_type=Application.GRANT_PASSWORD)
            return get_access_token(user)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("check your user name and password")
   
@protected_resource()
def sign_out(request):
    token= request.META['HTTP_AUTHORIZATION'].split(" ")[1]
    remove_access_token(token)
    #logout(request)
    return HttpResponse('Secret contents!', status=200)   
