from rest_framework import serializers
from .models import Job
from .models import Category

 
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'job_reference','job_title','job_cost' )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category_name','image')
