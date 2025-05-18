from django.shortcuts import render


def index(request):
    
    return render(request, 'core/index.html')


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        teamname = request.POST.get('teamname')
        password = request.POST.get('password')

        user = authenticate(request, username=teamname, password=password)

        if user is not None:
            login(request, user)
            return redirect('core:index')  # change this to wherever you want to redirect after login
        else:
            messages.error(request, 'Invalid team name or password.')

    return render(request, 'core/login.html')  # your login form template

def logout_view(request):
    logout(request)
    return redirect('core:login')  # back to login page

from .models import Challenge
def challenges(request):
    challenges = Challenge.objects.all()  # Assuming you have a Challenge model
    return render(request, 'core/challenges.html', {'challenges': challenges})

def challenge_details(request , pk):
    challenge = Challenge.objects.get(pk=pk)  # Assuming you have a Challenge model
    
    hints = challenge.hint_set.all()  

    return render(request, 'core/challenge_details.html', {'challenge': challenge, 'hints': hints})
