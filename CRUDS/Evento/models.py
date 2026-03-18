from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_maxima = models.IntegerField()
    descripcion = models.CharField(max_length=155)
    fecha = models.DateTimeField(auto_now_add=True)
    hora_inicio = models.TimeField(auto_now_add=True)
    precio_boleta = models.IntegerField()
    imagen = models. ImageField(upload_to="EventosApp")