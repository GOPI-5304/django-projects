from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'cal.html')

def add(request):
    if request.method=='POST':
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        operation=request.POST['operation']
        
        if operation == 'add':
            res = num1+num2
        elif operation == 'substraction':
            res = num1-num2
        elif operation == 'multiplication':
            res = num1*num2
        elif operation == 'division':
            if num2!=0:
                res = num1/num2
            else:
                res = "the number cannot be devided by zero"
        else:
            res = "invalid credentials"   
        
        return render(request,'cal.html',{'result':res})  
    return render(request, 'cal.html')

        
    

