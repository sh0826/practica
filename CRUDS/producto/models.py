from django.db import models

# Create your models here.
class Producto (models.Model):
    tipo_Producto = [
        ('cerveza', 'Cerveza'),
        ('licor', 'Licor'),
        ('cigarrillo', 'Cigarrillos')
    ]

    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30, choices=tipo_Producto)
    stock = models.IntegerField()
    precio_uni = models.IntegerField()
    imagen = models.ImageField(upload_to="ProductoApp")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    def __str__(self):
        return self.nombre
