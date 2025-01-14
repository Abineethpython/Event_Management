from django.db import models

# Create your models here.
class event(models.Model):
    image=models.ImageField(upload_to='media/')
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name=models.CharField(max_length=50)
    cus_ph=models.CharField(max_length=10)
    name=models.ForeignKey(event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)