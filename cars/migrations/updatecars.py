from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

def update_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_app/update_car.html', {'form': form})