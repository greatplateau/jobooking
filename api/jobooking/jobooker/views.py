from django.http import HttpResponse
from jobooker.models import Jobooker
from jobooker.serializer import JobookerSerializer
from rest_framework import generics, permissions


class JobookerList(generics.ListCreateAPIView):
    serializer_class = JobookerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        return Jobooker.objects.filter(owner=user)
    


class JobookerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = JobookerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Jobooker.objects.filter(owner=user)




