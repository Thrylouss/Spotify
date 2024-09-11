import math

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from librosa.core.audio import get_duration


# Create your models here
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='artists/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)

    def get_albums(self):
        return Album.objects.filter(artist=self)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='albums/', null=True, blank=True)
    artist = models.ManyToManyField(Artist)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def get_tracks_count(self):
        return Track.objects.filter(album=self).count()

    def get_tracks(self):
        return Track.objects.filter(album=self)

    def get_tracks_total_duration(self):
        tracks = self.get_tracks()
        if tracks:
            total_duration = sum(get_duration(filename=str(track.audio.path)) for track in tracks)
            print(total_duration)
            total_min = round(total_duration / 60)
            total_sec = round(total_duration % 60)
            return f"{total_min} min. {total_sec} sec."
        else:
            return 0

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=50)
    audio = models.FileField(upload_to='tracks/')
    lyrics = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    artist = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField()

    def get_duration(self):
        total = get_duration(filename=str(self.audio.path))
        total_min = math.floor(total / 60)
        total_sec = math.floor(total % 60)
        return f"{total_min} min. {total_sec} sec."

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ManyToManyField(Track)
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='playlists/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.name