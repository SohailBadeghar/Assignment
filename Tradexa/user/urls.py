

from django.urls import path
from .views import *

urlpatterns = [
    path('loginpage/', login_page,name="loginpage"),
    path('logout_page/',logout_page,name="logout_page"),
    path('', dashboard,name="dashboard"),
    
]