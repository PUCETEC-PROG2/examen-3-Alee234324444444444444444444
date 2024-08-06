from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect
from .forms import AlbumForm, ArtistForm
from .models import Artist, Album

def index(request):
    albums = Album.objects.order_by('title')
    template = loader.get_template('index.html')
    context = {'albums': albums}
    return HttpResponse(template.render(context, request))

def album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    template = loader.get_template('display_album.html')
    context = {'album': album}
    return HttpResponse(template.render(context, request))

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm()
    template = loader.get_template('album_form.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def edit_album(request, id):
    album = get_object_or_404(Album, pk=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm(instance=album)
    template = loader.get_template('album_form.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def delete_album(request, id):
    album = get_object_or_404(Album, pk=id)
    album.delete()
    return redirect('album_manager:index')

def artists_list(request):
    artists = Artist.objects.all()
    template = loader.get_template('artists_list.html')
    context = {'artists': artists}
    return HttpResponse(template.render(context, request))

def artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    template = loader.get_template('display_artist.html')
    context = {'artist': artist}
    return HttpResponse(template.render(context, request))

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artists_list')
    else:
        form = ArtistForm()
    template = loader.get_template('artist_form.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def edit_artist(request, id):
    artist = get_object_or_404(Artist, pk=id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artists_list')
    else:
        form = ArtistForm(instance=artist)
    template = loader.get_template('artist_form.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def delete_artist(request, id):
    artist = get_object_or_404(Artist, pk=id)
    artist.delete()
    return redirect('album_manager:artists_list')

