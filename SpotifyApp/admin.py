from django.contrib import admin

from SpotifyApp.models import Genre, Artist, Album, Track, Favorite, Playlist

# Register your models here.
admin.site.register([Genre, Artist, Album, Track, Favorite, Playlist])