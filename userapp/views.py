from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
def user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'UserName already exist')
                return redirect('register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register/')
            else:
                user_reg=User.objects.create_user(username=username,password=password,email=email)
                user_reg.save()
                messages.info(request, 'Successfully Registered')
                return redirect('/')
        else:
            messages.info(request, 'Wrong Password')
            return redirect('register/')
    return render(request, 'Register.html')

