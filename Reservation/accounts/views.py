# authentication/views.py
from django.shortcuts import render,redirect
from .models import*

from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse



def home(request):
    return render(request,'homepage.html')
def useregister(request):
     return render(request,'chooserole.html') 



def register_farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FarmerForm()

    return render(request, 'farmer/registerfarmer.html', {'form': form})



def register_driver(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Create a success template and URL
    else:
        form = FarmerForm()

    return render(request, 'driver/registerdriver.html', {'form': form})


