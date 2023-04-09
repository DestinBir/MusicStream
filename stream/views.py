from django.shortcuts import render, redirect
from .models import *


def home(request):
    artist = Artist.objects.afirst()

    return render(request, 'stream/index.html', context={'artist': artist})


def stream(request):
    artist = Artist.objects.afirst()
    musics = Music.objects.afirst()

    return render(request, 'stream/stream.html', context={'artist': artist, 'song': musics})
