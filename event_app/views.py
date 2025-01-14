from django.shortcuts import render
from . models import event

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def event_list(request):
    events=event.objects.all()
    context={
        'eve': events
    }
    return render(request,"events.html",context)

def booking(request):
    return render(request,"booking.html")

def register(request):
    return render(request,"Register.html")
