from django.db import models

class Artist(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    spotify_link = models.URLField(max_length=100)
    youtube_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    facebook_link = models.URLField(max_length=150)

    def __str__(self) -> str:
        return self.name

class Music(models.Model):
    picture = models.ImageField()
    song = models.FileField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
