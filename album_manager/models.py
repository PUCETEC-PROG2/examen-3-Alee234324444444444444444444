from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=40, null=False)
    country = models.CharField(max_length=30, null=False)
    birth = models.DateField(null=False)
    picture = models.ImageField(upload_to='artist_images')
    
    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=50, null=False)
    year = models.DateField(null=False)
    gender = models.CharField(max_length=30, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='album_images')
    
    def __str__(self) -> str:
        return self.title

    
 