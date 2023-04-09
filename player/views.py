from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import *


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        visitor = authenticate(username=username, email=email, password=password)
        if visitor:
            login(request, visitor)
            redirect('streaming_page')

    return render(request, 'player/login.html')
