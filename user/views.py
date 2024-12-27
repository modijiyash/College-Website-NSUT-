from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def homePage(request):
    return render(request, 'user/homepage.html')

def signup(request):
    if request.method=="POST":
        username = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']

        if User.objects.filter(username=username):
            messages.error(request, "Username already in use.")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already in use")
            return redirect('home')
        
        if password1!=password2:
            messages.error(request, "Passwords doesnt match")
            return redirect('signup')


        
        myuser = User.objects.create_user(username,email,password1)
        myuser.save()
        
        messages.success(request, "Account has been created succesfully")
        return redirect('login')

    return render(request, 'user/register.html')
    
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(username=username, password=password)
        
        if user is not None:

            auth_login(request, user)
            return render(request,'user/homepage.html')
        
        else:
            messages.error(request,"Wrong credentials")
            return redirect('home')
    return render(request, 'user/login.html')


def home(request):

    return render(request, "user/home.html")

def attendance(request):
    return render(request, "user/attendance.html")

def resoures(request):
    return render(request, "user/resoures.html")

def myprof(request):
    return render(request, "user/myprof.html")

def eventsfinal(request):
    return render(request, "user/eventsfinal.html")

def networking(request):
    return render(request, "user/networking.html")
