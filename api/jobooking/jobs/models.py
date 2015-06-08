from django.db import models

# Create your models here.

class Job(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    job_reference = models.CharField(max_length=100, default='')
    job_title = models.CharField(max_length=100, default='')
    job_cost = models.DecimalField(max_digits=7, decimal_places=2)
    owner =  models.ForeignKey('auth.User', related_name="jobs")
    category = models.ForeignKey('Category',default='')
    class Meta:
        ordering = ('created',)   

class Category(models.Model):
    category_name = models.CharField(max_length=100,default='')

