# vehicle/views.py
from django.shortcuts import render, redirect
from .forms import VehicleForm
from django.contrib.auth.decorators import login_required
from .models import Vehicle


@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.driver = request.user
            vehicle.save()
            return redirect('home_driver')  # หรือไปยัง URL ที่คุณต้องการ
    else:
        form = VehicleForm(initial={'driver': request.user})  # ส่งชื่อคนขับใน initial data
    return render(request, 'driver/add_vehicle.html', {'form': form})

