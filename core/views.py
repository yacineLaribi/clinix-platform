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
    for challenge in challenges:
        challenge.is_submitted = Submission.objects.filter(user=request.user, challenge=challenge).exists()

    return render(request, 'core/challenges.html', {'challenges': challenges})

from .models import Hint, Submission
def challenge_details(request , pk):
    challenge = Challenge.objects.get(pk=pk)  # Assuming you have a Challenge model
    is_submitted = False
    hints = challenge.hint_set.all()  

    if request.method == 'POST':
        diagnosis = request.POST.get('diagnosis')
        user = request.user
        if user.is_authenticated:

            submission = Submission(user=user, challenge=challenge, solution=diagnosis)
            submission.save()
            messages.success(request, 'Your submission has been recorded.')
        else:
            messages.error(request, 'You need to be logged in to submit a solution.')

    if request.user.is_authenticated:
        is_submitted = Submission.objects.filter(user=request.user, challenge=challenge).exists()
    else:
        is_submitted = False


    return render(request, 'core/challenge_details.html', {'challenge': challenge, 'hints': hints , 'is_submitted': is_submitted})
