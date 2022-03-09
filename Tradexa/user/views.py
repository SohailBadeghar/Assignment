from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login,logout as django_logout
from django.views.decorators.csrf import csrf_exempt
from .models import Post_Model_User,User_Model
from django.contrib import messages

# Create your views here.


@csrf_exempt
def dashboard(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            print(request.user.is_authenticated)
            text = request.POST.get('text')
            k = User_Model.objects.get(id=request.user.id)
            a = Post_Model_User.objects.create(user = k,text = text)
            messages.success(request, 'Succesfully Posted')
            return redirect('dashboard')
        else:
            messages.error(request, 'please login before post ')
            return redirect('dashboard')
    else:
        return render(request,'user/dashboard.html')



@csrf_exempt
def login_page(request):
    print(request.user)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            django_login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'user/login.html')
    else:
        return render(request,'user/login.html')
    
    
def logout_page(request):
    django_logout(request)
    return redirect('loginpage')