from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_car, name='create_car'),
    path('', views.car_list, name='car_list'),
    path('update/<int:car_id>/', views.update_car, name='update_car'),
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),
]