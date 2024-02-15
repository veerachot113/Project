# # driver/views.py

# from django.shortcuts import render, redirect
# from .forms import VehicleForm
# from django.contrib.auth.decorators import login_required
# from .models import Vehicle

# @login_required
# def home(request):
#     latest_vehicle = Vehicle.objects.latest('id')
#     return render(request, 'driver/home.html', {'latest_vehicle': latest_vehicle})

# @login_required
# def home_driver(request):
#     vehicles = Vehicle.objects.filter(user=request.user)
#     return render(request, 'driver/home_driver.html', {'vehicles': vehicles})

# @login_required
# def add_vehicle(request):
#     if request.method == 'POST':
#         form = VehicleForm(request.POST, request.FILES)
#         if form.is_valid():
#             vehicle = form.save(commit=False)
#             vehicle.user = request.user
#             vehicle.save()
#             return redirect('home')
#     else:
#         form = VehicleForm()
#     return render(request, 'driver/add_vehicle.html', {'form': form})




