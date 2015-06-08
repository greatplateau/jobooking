from rest_framework import serializers
from .models import Jobooker
from django.contrib.auth.models import User 
 
class JobookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobooker
        fields = ('id', 'firstName')

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', )
