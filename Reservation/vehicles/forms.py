# vehicle/forms.py

from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['driver','image', 'model', 'type', 'price', 'province']
