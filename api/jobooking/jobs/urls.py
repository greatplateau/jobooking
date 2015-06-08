from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.JobList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.JobDetail.as_view()),   
    url(r'category/', views.CategoryList.as_view()),
]


