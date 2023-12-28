

from django.shortcuts import render, redirect
from .models import user

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        u = user(username=username, email=email, password=password)
        u.save()
        return redirect('login')
    return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_exists=user.objects.filter(username=username,password=password)
        if user_exists:
            return render(request,'home.html')
    return render(request,'login.html')

        
