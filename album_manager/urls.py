from django.urls import path
from . import views

app_name = 'album_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('album/<int:album_id>/', views.album, name='album'),
    path('album/add/', views.add_album, name='add_album'),
    path('album/<int:id>/edit/', views.edit_album, name='edit_album'),
    path('album/<int:id>/delete/', views.delete_album, name='delete_album'),
    path('artists/', views.artists_list, name='artists_list'),
    path('artist/<int:artist_id>/', views.artist, name='artist'),
    path('artist/add/', views.add_artist, name='add_artist'),
    path('artist/<int:id>/edit/', views.edit_artist, name='edit_artist'),
    path('artist/<int:id>/delete/', views.delete_artist, name='delete_artist'),
]



