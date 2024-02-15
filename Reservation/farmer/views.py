#farmerbooling/views
from django.shortcuts import render, redirect
from vehicles.models import*
from .models import*


def booking(request,id):
    vehicles = Vehicle.objects.get(pk=id)
    if request.method == 'POST':
        name = request.user
        fullname = request.POST.get('fullname')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        phone = request.POST.get('phone')
        details = request.POST.get('details')
    
        b = Booking.objects.create(
            name=name,
            fullname=fullname,
            address =address ,
            quantity= quantity,
            phone=phone,
            details=details,
            vehicle=vehicles
            )
        b.save()
        return redirect('showbooking')  # หรือไปยัง URL ที่คุณต้องการ
   
    return render(request, 'farmer/booking.html',{'vehicles':vehicles})



def showbooking(request):
    booking = Booking.objects.filter(name=request.user)
    return render(request, 'farmer/showbooking.html',{'booking':booking})













def booking_success(request):
    return render(request, 'booking_success.html')

