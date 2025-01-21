from django.shortcuts import render,redirect
from . models import event
from . forms import BookingForm
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,"about.html")

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, 'user successfully logged-in')
            return redirect('/')
        else:
            messages.info(request, 'Invalid User credentials')
            return redirect('register/')


    return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def event_list(request):
    events=event.objects.all()
    context={
        'eve': events
    }
    return render(request,"events.html",context)

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=BookingForm
    dict_form={
        'form':form
    }

    return render(request,"booking.html",dict_form)

def register(request):
    return render(request,"Register.html")
