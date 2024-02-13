# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import UserFarmerRegistrationForm, UserDriverRegistrationForm
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group  # Add this import
from django.contrib.auth.decorators import login_required

@login_required
def custom_logout(request):
    logout(request)
    return redirect('home')  
# def home(request):
#     return render(request, 'templates/components/base.html')

def home(request):
    return render(request, 'accounts/home.html')
@login_required
def home_farmer(request):
    return render(request,'farmer/home_farmer.html')
@login_required
def home_driver(request):
    return render(request,'driver/home_driver.html')


def useregister(request):
     return render(request,'accounts/chooserole.html') 


def register_farmer(request):
    if request.method == 'POST':
        form = UserFarmerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Add the user to the 'driver' group
            farmer_group = Group.objects.get(name='farmer')
            user.groups.add(farmer_group)
            
            return redirect('login')
    else:
        form = UserFarmerRegistrationForm()

    return render(request, 'farmer/registerfarmer.html', {'form': form})

def register_driver(request):
    if request.method == 'POST':
        form = UserDriverRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            driver_group = Group.objects.get(name='driver')
            user.groups.add(driver_group)

            return redirect('login')
    else:
        form = UserDriverRegistrationForm()

    return render(request, 'driver/registerdriver.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # Additional logging for debugging
                print(f"User {username} logged in with groups: {[group.name for group in user.groups.all()]}")

                # Check all group names
                print(f"All group names: {[group.name for group in Group.objects.all()]}")

                # Check the user's role and redirect accordingly
                if 'farmer' in [group.name for group in user.groups.all()]:
                    return redirect('home_farmer')
                elif 'driver' in [group.name for group in user.groups.all()]:
                    return redirect('home_driver')
                else:
                    return redirect('home')  # Default redirect if not in any group

            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/registration/login.html', {'form': form})








@login_required
def profile_update(request):
    form = None
    if 'farmer' in [group.name for group in request.user.groups.all()]:
        if request.method == 'POST':
            form = UserFarmerUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile_update')
        else:
            form = UserFarmerUpdateForm(instance=request.user)
    elif 'driver' in [group.name for group in request.user.groups.all()]:
        if request.method == 'POST':
            form = UserDriverUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile_update')
        else:
            form = UserDriverUpdateForm(instance=request.user)

    
    return render(request,'accounts/profile_driver.html', {'form': form})





