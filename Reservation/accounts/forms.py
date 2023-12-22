# custom_users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserFarmer, UserDriver

class UserFarmerRegistrationForm(UserCreationForm):
    # add custom fields for farmer registration
    class Meta:
        model = UserFarmer
        fields = ['username', 'email', 'password1', 'password2']

class UserDriverRegistrationForm(UserCreationForm):
    # add custom fields for driver registration
    class Meta:
        model = UserDriver
        fields = ['username', 'email', 'password1', 'password2']
