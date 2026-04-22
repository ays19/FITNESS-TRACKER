from django.shortcuts import render, redirect
from .models import Workout
from .forms import WorkoutForm

# VIEW TO LIST WORKOUTS
def workout_list(request):
    workouts= Workout.objects.all().order_by('-date')
    return render(request, 'tracker/workout_list.html', {'workouts': workouts})

# view to add a workout
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        print("POST data:", request.POST)       # check data is coming in
        print("Form valid:", form.is_valid())    # check if valid
        print("Form errors:", form.errors) 
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'tracker/add_workout.html',{'form': form})