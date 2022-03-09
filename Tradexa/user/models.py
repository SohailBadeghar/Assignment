from pyexpat import model
from django.db import models


class User_Model(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=True)
    lastname = models.CharField(max_length=50, blank=False, null=True)
    email = models.CharField(max_length=50, blank=False, null=True)
    username = models.CharField(max_length=50, blank=False, null=True)
    password = models.CharField(max_length=50, blank=False, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.username

class Post_Model_User(models.Model):
    user = models.ForeignKey("User_Model",on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add= True,blank=False, null=True)
    updated_at = models.DateTimeField(auto_now= True,blank=False, null=True)
