from django.shortcuts import render, redirect
from .models import Car

def delete_car(request, car_id):
    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect('car_list')