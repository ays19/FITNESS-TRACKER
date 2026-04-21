from django.shortcuts import render, redirect
from .models import Workout
from .forms import WorkoutForm

# VIEW TO LIST WORKOUTS
def workout_list(request):
    workout= Workout.objects.all().order_by('-date')
    return render(request, 'tracker/workout_list.html', {'workouts': workout})

# view to add a workout
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
        else:
            form = Workout()
        return render(request, 'tracker/add_workout.html',{'form': form})