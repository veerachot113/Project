# driver/forms.py
# from django import forms
# from .models import Vehicle

# class VehicleForm(forms.ModelForm):
#     class Meta:
#         model = Vehicle
#         fields = ['image', 'model', 'type', 'price', 'province']
# class AddPetForm(forms.ModelForm):
#     class Meta:
#         model = Pet
#         fields = '__all__'
    
#         widgets = {
#         'date_time':forms.TextInput(attrs={'type': 'datetime-local'})
#         }

#         labels = {
#             'name' : 'ชื่อ',
#             'age' : 'อายุ',
#             'profile' : 'รูป',
#             'sex' : 'เพศ',
#             'breed' : 'สายพันธุ์',
#             'desc' : 'คำอธิบาย',
#             'date_time': 'วัน-เวลา', 
#             'appear' : 'แสดง',
#         }