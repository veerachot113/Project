# driver/views.py
from django.shortcuts import render, redirect
from .forms import VehicleForm
from accounts.models import *
from django.contrib.auth.decorators import login_required
from .models import Vehicle

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'templates/homepage/vehicle_list.html', {'vehicles': vehicles})


@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            # Assuming you have a way to get the logged-in user (driver)
            logged_in_user = request.user  # Replace this with your actual way to get the logged-in user

            # Set the driver field before saving the form
            form.instance.driver = logged_in_user
            form.save()

            return redirect('vehicle_list')
    else:
        form = VehicleForm()

    return render(request, 'templates/driver/add_vehicle.html', {'form': form})
