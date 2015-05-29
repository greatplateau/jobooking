from rest_framework import serializers
from .models import Jobooker
 
 
class JobookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobooker
        fields = ('id', 'firstName')
