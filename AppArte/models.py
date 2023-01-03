from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Libros(models.Model):
    
    def __str__(self):
        
        return f'Nombre: {self.nombre} --- Autor:{self.autor}'
    
    nombre=models.CharField(max_length=70)
    autor=models.CharField(max_length=70)
    año=models.IntegerField()
    genero=models.CharField(max_length=70)
    puntaje= models.FloatField()
    descripcion= models.TextField()
    usuarioBlog = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    portada= models.ImageField(upload_to="libros/", null=True, blank=True)


class Discos(models.Model):
    
    def __str__(self):
        
        return f'Nombre: {self.nombre} --- Artista:{self.artista}'
    
    nombre=models.CharField(max_length=70)
    artista=models.CharField(max_length=70)
    año=models.IntegerField()
    genero=models.CharField(max_length=70)    
    puntaje= models.FloatField()
    descripcion= models.TextField()
    usuarioBlog = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tapa= models.ImageField(upload_to="discos/", null=True, blank=True)

class Pinturas(models.Model):
    
    def __str__(self):
        
        return f'Nombre: {self.nombre} --- Artista:{self.artista}'
    
    nombre=models.CharField(max_length=70)
    artista=models.CharField(max_length=70)
    año=models.IntegerField()
    descripcion= models.TextField()
    usuarioBlog = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    foto= models.ImageField(upload_to="pinturas/", null=True, blank=True)

class Avatar(models.Model):
    
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="avatares", null=True, blank=True)