from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import *


def home(request):
    artist = Artist.objects.get(id=2)

    return render(request, 'stream/index.html', context={'artist': artist})


def stream(request):
    artist = Artist.objects.get(id=2)
    musics = Music.objects.all()

    return render(request, 'stream/stream.html', context={'artist': artist, 'song': musics})
