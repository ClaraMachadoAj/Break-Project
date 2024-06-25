from django.db import models

# Create your models here.
class Album(models.Model):
    titulo = models.CharField(max_length = 200, null = None)
    artista = models.TextField(null = None)
    genero = models.CharField(max_length = 20, null = None)


class Musica(models.Model):
    titulo = models.CharField(max_length = 200, null = None)
    compositor = models.TextField(null = None)
    duracao = models.SmallIntegerField()
    album = models.ForeignKey(Album, on_delete = models.CASCADE) 
