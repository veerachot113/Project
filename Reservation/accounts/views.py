from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserFarmerRegistrationForm, UserDriverRegistrationForm


# accounts/views.py



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

    return render(request, 'templates/farmer/registerfarmer.html', {'form': form})

def register_driver(request):
    if request.method == 'POST':
        form = UserDriverRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Add the user to the 'driver' group
            driver_group = Group.objects.get(name='driver')
            user.groups.add(driver_group)

            return redirect('login')
    else:
        form = UserDriverRegistrationForm()

    return render(request, 'templates/driver/registerdriver.html', {'form': form})







def custom_logout(request):
    logout(request)
    return redirect('home')  

def home(request):
    return render(request,'templates/accounts/home.html')

def home_farmer(request):
    return render(request,'templates/farmer/home_farmer.html')

def home_driver(request):
    return render(request,'templates/driver/home_driver.html')


def useregister(request):
     return render(request,'templates/accounts/chooserole.html') 



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

#เอา def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Welcome back, {username}!")
#                 return redirect('home')  # Redirect to the home page or any desired URL after login
#             else:
#                 messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
    
#     return render(request, 'templates/accounts/registration/login.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group  # Add this import

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
    
    return render(request, 'templates/accounts/registration/login.html', {'form': form})



# def register(request):
#     if request.method == 'POST':
#         user_form = RegistrationForm(request.POST)

#         if user_form.is_valid():
#             user = user_form.save()

#             login(request, user)
#             return redirect('home')  # Change 'home' to the URL you want to redirect to after registration
#     else:
#         user_form = RegistrationForm()


#     return render(request, 'register.html', {'user_form': user_form})


# def register(request):
#      if request.method == 'POST':
#          form = FarmerForm(request.POST)
#          if form.is_valid():
#              form.save()
#              return redirect('home')
#      else:
#          form = FarmerForm()
#      return render(request, 'register.html', {'form': form})




# def register_farmer(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         return render(request, 'farmer/registerfarmer.html', { 'form': form})     
   
#     if request.method == 'POST':
#         form = RegisterForm(request.POST) 
#         if form.is_valid():
#             user = form.save()
#             user.username = user.username.lower()
#             messages.success(request, 'You have signed up successfully.')
#             login(request, user)
#             return redirect('login')
#         else:
#             messages.error(request, 'There was an error in the form submission.')
#             print(form.errors)
#     return render(request, 'farmer/registerfarmer.html', {'form': form})


# def register_driver(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         return render(request, 'driver/registerdriver.html', { 'form': form})     
   
#     if request.method == 'POST':
#         form = RegisterForm(request.POST) 
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             messages.success(request, 'You have singed up successfully.')
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'driver/registerdriver.html', { 'form': form})

# def register_farmer(request):
#     if request.method == 'POST':
#         form = FarmerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = FarmerForm()

#     return render(request, 'farmer/registerfarmer.html', {'form': form})



# def register_driver(request):
#     if request.method == 'POST':
#         form = FarmerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Create a success template and URL
#     else:
#         form = FarmerForm()

#     return render(request, 'driver/registerdriver.html', {'form': form})

# def testform(request):
#     forms = Formss()

#     return render(request,'register.html',{'form':forms})


