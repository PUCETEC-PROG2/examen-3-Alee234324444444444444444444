from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AlbumForm, ArtistForm
from .models import Artist, Album

def index(request):
    albums = Album.objects.order_by('title') 
    return render(request, 'index.html', {'albums': albums})

def album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)  
    return render(request, 'display_album.html', {'album': album})

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index') 
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})

def edit_album(request, id):
    album = get_object_or_404(Album, pk=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')  
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})

def delete_album(request, id):
    album = get_object_or_404(Album, pk=id)
    album.delete()
    return redirect('album_manager:index') 

def artists_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists_list.html', {'artists': artists})

def artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'display_artist.html', {'artist': artist})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artists_list')  
    else:
        form = ArtistForm()
    return render(request, 'artist_form.html', {'form': form})

def edit_artist(request, id):
    artist = get_object_or_404(Artist, pk=id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artists_list')  
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artist_form.html', {'form': form})

def delete_artist(request, id):
    artist = get_object_or_404(Artist, pk=id)
    artist.delete()
    return redirect('album_manager:artists_list')  
