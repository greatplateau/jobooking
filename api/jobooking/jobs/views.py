from django.http import HttpResponse
from jobs.models import Job
from jobs.serializer import JobSerializer
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




