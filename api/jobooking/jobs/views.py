from django.http import HttpResponse
from jobs.models import Job
from jobs.models import Category
from jobs.serializer import JobSerializer
from jobs.serializer import CategorySerializer
from rest_framework import generics, permissions


class JobList(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        return Job.objects.filter(owner=user)
    


class JobDetail(generics.RetrieveDestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Jobooker.objects.filter(owner=user)

class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.all()
