from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from uploads.models import UploadItem
from uploads.forms import UploadItemForm 
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        c=User.objects.create_user(username=username,email=email,password=password)
        c.save()
        messages.success(request,'Your account has been created successfully! Please Login to Continue...')
        return redirect('login')
    return render(request,'register.html')


def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('uploads')
        else:
            messages.error(request,"Username or password didn't match!")            
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def uploads(request):
    if request.method=='POST':
        form=UploadItemForm(request.POST, request.FILES)
        form.instance.uploaded_by = request.user
        if form.is_valid():
            form.save()      
            messages.success(request,'Your file upload is successful..!') 
            form=UploadItemForm()
        else:
              messages.error(request,'Invalid..!') 
            
    else:
        form=UploadItemForm()

    context={'form':form}
    return render(request,'uploads.html',context)
 
