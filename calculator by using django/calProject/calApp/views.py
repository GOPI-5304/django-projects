from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'cal.html')
def add(request):
    val1=int(request.GET["num1"])
    val2=int(request.GET["num2"])
    
    result=val1+val2
    
    return render(request,'result.html',{'result':result})