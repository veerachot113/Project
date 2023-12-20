 # urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    #path('login/',user_login,name='login'),
    #path('logout/',sign_out,name='logout'),
    path('registerfarmer/',register_farmer,name='registerfarmer'),
    path('registerdriver/',register_driver,name='registerdriver'),
    path('useregister/',useregister,name='chooserole'),
    #path('choose-role/', choose_role, name='choose_role'),
]