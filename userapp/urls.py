from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.user,name='register'),

]