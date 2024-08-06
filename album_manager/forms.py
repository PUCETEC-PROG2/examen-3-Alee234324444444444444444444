from django import forms
from .models import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

