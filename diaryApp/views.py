from django.shortcuts import render,redirect
from .models import Memory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required(login_url='/accounts/login')
def show(request):
    logged_user = request.user
    print(logged_user)
    memories = Memory.objects.filter(user=logged_user)
    return render(request,'mydiary.html',{'memories':memories,'username':request.user.first_name})

@login_required(login_url='/accounts/login')
def add(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        print(data)
        currUser = Memory(content=data,user=request.user)
        currUser.save()
        return redirect(show)
        
    else:
        return render(request,'addmemory.html',{'username':request.user})


@login_required(login_url='/accounts/login')
def updateMemory(request,id):
    if request.method == 'POST':
        updatedContent = request.POST.get('updatedContent')
        currMemory = Memory.objects.get(pk=id)
        currdate = datetime.date.today()
        currMemory.content = updatedContent
        currMemory.date = str(currdate)
        print(currdate)
        currMemory.save()
        return redirect(show)
    else:
        currMemory = Memory.objects.get(pk=id)
        return render(request,'update.html',{'data':currMemory})





@login_required(login_url='/accounts/login')
def deleteMemory(request,id):
    if request.method == 'POST':
        currMemory = Memory.objects.get(pk=id)
        currMemory.delete()
        return redirect(show)

