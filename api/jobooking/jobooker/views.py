from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from jobooker.models import Jobooker
from jobooker.serializer import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .tools import get_access_token
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SigninForm
from oauth2_provider.models import Application


@api_view(['POST'])
def create_jobooker(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        serialized.save()
#        User.objects.create_user(
 #           serialized.init_data['email'],
 
#           serialized.init_data['username'],
 #           serialized.init_data['password']
  #      )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
    


def sign_in(request):

    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
	            login(request,user)
                    Application.objects.filter(user_id = user.id).delete()
                    Application.objects.create(user=user,name="jobooker", 
                                   client_type=Application.CLIENT_CONFIDENTIAL,
                                   authorization_grant_type=Application.GRANT_PASSWORD)
                    return get_access_token(user)
                else:
                    return HttpResponse("error")

    else:
        form = SigninForm()

    return render(request, 'signin.html', {
        'form': form,
    }) 



