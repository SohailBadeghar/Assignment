from django.contrib import admin
from .models import User_Model,Post_Model_User
# Register your models here.

admin.site.register(User_Model)
admin.site.register(Post_Model_User)