from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    spotify_link = models.URLField(max_length=100)
    youtube_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    facebook_link = models.URLField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'


class Music(models.Model):
    picture = models.ImageField(blank=False, upload_to='music')
    song = models.FileField( blank=False, upload_to='music')
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'
