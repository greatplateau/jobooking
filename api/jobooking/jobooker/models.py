from django.db import models

# Create your models here.

class Jobooker(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField(max_length=100, default='')
    owner =  models.ForeignKey('auth.User', related_name="jobooker",default='')
    class Meta:
        ordering = ('created',)
