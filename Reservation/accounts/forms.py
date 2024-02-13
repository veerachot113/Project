# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserFarmer, UserDriver

class UserFarmerRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, label='ชื่อ-สกุล')  # เพิ่มชื่อ-สกุล
    address = forms.CharField(max_length=255, required=True, label='ที่อยู่')  # เพิ่มที่อยู่
    phone = forms.CharField(max_length=15, required=True, label='เบอร์โทรศัพท์')  # เพิ่มเบอร์โทรศัพท์

    class Meta:
        model = UserFarmer
        fields = ['username', 'email', 'password1', 'password2', 'name', 'address', 'phone']

class UserFarmerUpdateForm(UserChangeForm):
    name = forms.CharField(max_length=100, required=True, label='ชื่อ-สกุล')  # เพิ่มชื่อ-สกุล
    address = forms.CharField(max_length=255, required=True, label='ที่อยู่')  # เพิ่มที่อยู่
    phone = forms.CharField(max_length=15, required=True, label='เบอร์โทรศัพท์')  # เพิ่มเบอร์โทรศัพท์

    class Meta:
        model = UserFarmer
        fields = ['username', 'email', 'name', 'address', 'phone']

class UserDriverRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, label='ชื่อ-สกุล')  # เพิ่มชื่อ-สกุล
    address = forms.CharField(max_length=255, required=True, label='ที่อยู่')  # เพิ่มที่อยู่
    phone = forms.CharField(max_length=15, required=True, label='เบอร์โทรศัพท์')  # เพิ่มเบอร์โทรศัพท์

    class Meta:
        model = UserDriver
        fields = ['username', 'email', 'password1', 'password2', 'name', 'address', 'phone']

class UserDriverUpdateForm(UserChangeForm):
    name = forms.CharField(max_length=100, required=True, label='ชื่อ-สกุล')  # เพิ่มชื่อ-สกุล
    address = forms.CharField(max_length=255, required=True, label='ที่อยู่')  # เพิ่มที่อยู่
    phone = forms.CharField(max_length=15, required=True, label='เบอร์โทรศัพท์')  # เพิ่มเบอร์โทรศัพท์

    class Meta:
        model = UserDriver
        fields = ['username', 'email', 'name', 'address', 'phone']
