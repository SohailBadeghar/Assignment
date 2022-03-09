from operator import mod
from django.db import models

# Create your models here.

class Product_Model(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    weight = models.CharField(max_length=50,null=True,blank=True)
    price = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add= True,blank=False, null=True)
    updated_at = models.DateTimeField(auto_now_add= True,blank=False, null=True)