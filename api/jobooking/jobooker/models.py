from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Jobooker(models.Model):
     user = models.OneToOneField(User)
     phone_no = models.CharField(max_length=100)

#class User(models.Model):
#    username =  models.CharField(max_length=100)
#    password =  models.CharField(max_length=100)
#    email =  models.CharField(max_length=100)
#    def get_email():
#        return email

