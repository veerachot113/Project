# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home_farmer/', home_farmer, name='home_farmer'),# Provide a unique path for the farmer home
    path('HomeDriver/', home_driver, name='home_driver'),  # Provide a unique path for the driver home
    path('logout/', custom_logout, name='logout'),
    path('userlogin/', user_login, name='login'),
    path('registerfarmer/', register_farmer, name='registerfarmer'),
    #path('register/', register, name='register'),
    path('registerdriver/', register_driver, name='registerdriver'),
    path('useregister/', useregister, name='chooserole'),
    
]
