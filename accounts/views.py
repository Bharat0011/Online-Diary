from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from diaryApp.views import show

# Create your views here.
def home(request):
    return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect(show)
        else:
            return render(request,'login.html',{'error':'Username or Password not Correct'})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect(home)


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] ==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'register.html',{'error':'Username Already Taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],first_name = request.POST['fname'],last_name = request.POST['lname'])
                # to login user directly after signup
                auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect(login)
        else:
            return render(request,'register.html',{'error':'Passwords Dont Match'})
    else:
        return render(request,'register.html')


