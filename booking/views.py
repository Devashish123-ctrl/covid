from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .forms import UserSignupForm, UserLoginForm
from .models import VaccinationCenter, VaccinationSlot


def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_admin:
                    return redirect('admin-dosage-details')
                return redirect('centers')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def centers_view(request):
    centers = VaccinationCenter.objects.all()
    return render(request, 'centers.html', {'centers': centers})


def slots_view(request):
 if request.user != "":
    if request.method == 'POST':
        center_id = request.POST.get('center_id')
        date = request.POST.get('date')
        time_slot = request.POST.get('time_slot')
        center = VaccinationCenter.objects.get(id=center_id)
        if VaccinationSlot.objects.filter(center=center, date=date).count() < 10:
            VaccinationSlot.objects.create(user=request.user, center=center, date=date, time_slot=time_slot)
            return redirect('slots')
        else:
            return render(request, 'slots.html', {'error': 'All slots are booked for this date'})
    return render(request, 'slots.html')
 else:
     return redirect("login")




def user_logout(request):
    logout(request)
    return redirect('logout')
