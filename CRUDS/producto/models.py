from django.db import models

# Create your models here.
class Producto (models.Model):
    nombre = models.CharField(max_length=20)
    tipo_Producto = [
        ('cerveza', 'Cerveza'),
        ('licor', 'Licor'),
        ('cigarrillo', 'Cigarrillos')
    ]
    stock = models.IntegerField()
    precio_uni = models.IntegerField()
    imagen = models.ImageField(upload_to="ProductoApp")
