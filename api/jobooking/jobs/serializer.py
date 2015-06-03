from rest_framework import serializers
from .models import Job
 
 
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'job_reference','job_title','job_cost' )
