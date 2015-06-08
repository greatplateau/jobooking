from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
   url(r'^register', views.create_jobooker),
   url(r'^signin', views.sign_in),
   url(r'^signout', views.sign_out),    
]


