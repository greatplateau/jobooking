from django.db import models

# Create your models here.

class Job(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=1000, default='')
    title = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    CHARGETYPE = (
        (0, 'By Time'),
        (1, 'By Job'),
    )
    charge_type = models.DecimalField(max_digits=1, choices=CHARGETYPE, default=0, decimal_places=0)
    confirmation_time = models.DecimalField(max_digits=7,decimal_places=0,default=1440)
    owner =  models.ForeignKey('auth.User', related_name="jobs")
    category = models.ForeignKey('Category',default='')
    images = models.ForeignKey('Image', default='')
    class Meta:
        ordering = ('created',)   

class Category(models.Model):
    category_name = models.CharField(max_length=100,default='')
    image = models.CharField(max_length=1000,default='xxx/yyy')

class Image(models.Model):
    image_url = models.URLField(max_length=1000,default='')

