from django.contrib import admin
from .models import *

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'spotify_link', 'youtube_link', 'instagram_link', 'facebook_link')


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')
