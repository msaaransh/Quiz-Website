from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, "MainApp/home.html")

def all_quiz(request):
    return render(request, "MainApp/all_quiz.html")

def leaderboard(request):
    return render(request, "MainApp/leaderboard.html")

def profile(request):
    return render(request, "MainApp/profile.html")

def Quiz(request):
    return render(request, "MainApp/quiz.html")

def result(request):
    return render(request, "MainApp/result.html")

def submit(request):
    return render(request, "MainApp/submit.html")

def login(request):
    return render(request, "MainApp/login.html")

def sign_up(request):
    return render(request, "MainApp/sign_up.html")

def forgot(request):
    return render(request, "MainApp/forgot.html")

