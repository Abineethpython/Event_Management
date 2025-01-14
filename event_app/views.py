from django.shortcuts import render,redirect
from . models import event
from . forms import BookingForm

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
