import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Track, Artist, Album, Playlist, Genre


# Create your views here.
class SpotifyMainPageView(ListView):
    model = Album
    template_name = 'SpotifyApp/user/main_page.html'
    context_object_name = 'albums'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_playlists'] = Playlist.objects.filter(user=self.request.user)
        else:
            context['user_playlists'] = None
        new_data = datetime.date.today() - datetime.timedelta(days=3)
        context['tracks'] = Track.objects.all()
        context['new_releases'] = Album.objects.filter(created_at__gte=new_data)
        return context


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'SpotifyApp/user/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = Track.objects.all()
        if self.request.user.is_authenticated:
            context['user_playlists'] = Playlist.objects.filter(user=self.request.user)
        else:
            context['user_playlists'] = None
        return context


class TrackDetailView(DetailView):
    model = Track
    template_name = 'SpotifyApp/user/track_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_playlists'] = Playlist.objects.filter(user=self.request.user)
        else:
            context['user_playlists'] = None
        context['tracks'] = Track.objects.all()
        return context


def play_track(request, track_id):
    try:
        track = Track.objects.get(id=track_id)
        return JsonResponse({'status': 'success', 'track': track.audio.url, 'track_name': track.name,
                             'track_id': track.id,
                             'album_name': track.album.name, 'album_artist': track.album.artist.first().name,
                             'track_image': track.album.image.url})
    except Track.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Track not found'}, status=404)


def pause_track(request):
    return JsonResponse({'status': 'success', 'message': 'Paused'})


def next_track(request, current_track_id):
    try:
        current_track = Track.objects.get(id=current_track_id)
        next_track = Track.objects.filter(order__gt=current_track.order).order_by('order').first()
        if next_track:
            return JsonResponse({'status': 'success', 'track': next_track.audio.url, 'track_name': next_track.name,
                                 'album_id': next_track.album.id,
                                 'album_name': next_track.album.name,
                                 'album_artist': next_track.album.artist.first().name,
                                 'track_image': next_track.album.image.url})
        else:
            return JsonResponse({'status': 'error', 'message': 'No next track'}, status=404)
    except Track.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Track not found'}, status=404)


def previous_track(request, current_track_id):
    try:
        current_track = Track.objects.get(id=current_track_id)
        prev_track = Track.objects.filter(order__lt=current_track.order).order_by('-order').first()
        if prev_track:
            return JsonResponse({'status': 'success', 'track': prev_track.audio.url, 'track_name': prev_track.name,
                                 'album_id': prev_track.album.id,
                                 'album_name': prev_track.album.name,
                                 'album_artist': prev_track.album.artist.first().name,
                                 'track_image': prev_track.album.image.url})
        else:
            return JsonResponse({'status': 'error', 'message': 'No previous track'}, status=404)
    except Track.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Track not found'}, status=404)
