from django.shortcuts import render
from .forms import RegisterForm
from .models import User
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from django.contrib.auth.models import  auth
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           print('formis valid')
           form.save()
           email=form.cleaned_data.get('email')
           password=form.cleaned_data.get('password1')
           user=authenticate(email=email,password=password)
           login(request,user)
           return redirect('home')
        #    if  Users.objects.filter(email=request.POST['email']).exists():
        #        print("email is exixt")
               
        else:
            print("error")
    else:
        form = RegisterForm()
    return render(request,'main/register.html',{'form':form})

def Login(request):
    print("login form")
    context={}
    if request.method =="POST":
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            print("asdsdfsd",email)
            password=form.cleaned_data.get('password1')
            user=authenticate(email=email,password=password)
            login(request,user)
            return redirect('home')
        else:
            print("invalid")
            return redirect('login')
    else:
        form=AuthenticationForm()
        context['form']=form
    return render(request,'main/login.html',context)
    # if request.method =='POST':
    #     email=request.POST['email']
    #     print("sadfsadfsadfsadf",email)
    #     password= request.POST['password']
    #     user = auth.authenticate(email=email,password=password)
    #     print("login in ommm",user)
    #     if user:
    #             if user.is_active:
    #                 login(request,user)
    #                 print({"sdfsdf"})
                  
    #             else:
    #                 return redirect('login')
                   
    #     else:
    #         print("Someone tried to login and failed.")
    #         print("They used username: {} and password:")
    #         return redirect('login')
    # else:
    #     return render(request,'main/login.html')


def Logout(request):
    logout(request)
    return redirect('home')