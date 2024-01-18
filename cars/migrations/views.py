from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car_app/create_car.html', {'form': form})