from django.urls import path
from . import views

urlpatters = [
    path('', views.workout_list, name='workout_list'),
    path('add/', views.add_workout, name='add_workout'),
]