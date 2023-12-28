from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request,'index.html')
@api_view(['POST','GET'])
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            if not User.objects.filter(username=username).exists():
                messages.error(request,"invalid username")
        except:
            user=authenticate(username=username,password=password)
            return Response("invalid user name")
        try:
            if user is None:
                messages.error(request,"invalid password")
                # return redirect('login')
                Response("hello")
            else:
                return redirect("home")
        except:
            print("hello 25")
            # return render(request,'login.html')  
            return HttpResponse("login successfull")
    else:
        return render(request,'login.html')

@api_view(['POST','GET'])
def register(request):
    if request.method == "POST":
        uname=request.POST["username"]
        print(uname)
        email=request.POST["email"]
        password=request.POST["password"]
        if User.objects.filter(email=email,username=uname).exists():
            return render(request,"register.html")
        user=User.objects.create_user(username=uname,email=email,password=password)
        user.save()
        return HttpResponse('hello')
    
    # else:
    #     return render(request,'register.html')
    return HttpResponse("hello 2")
        