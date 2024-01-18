from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all().values('id', 'brand', 'year')
    return render(request, 'car_app/car_list.html', {'cars': cars})