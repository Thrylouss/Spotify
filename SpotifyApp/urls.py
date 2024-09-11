from django.urls import path
from . import views

urlpatterns = [
    path('', views.SpotifyMainPageView.as_view(), name='index'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('track/<int:pk>/', views.TrackDetailView.as_view(), name='track_detail'),
    path('play-track/<int:track_id>/', views.play_track, name='play_track'),
    path('pause-track/', views.pause_track, name='pause_track'),
    path('next-track/<int:current_track_id>/', views.next_track, name='next_track'),
    path('previous-track/<int:current_track_id>/', views.previous_track, name='previous_track'),
]
