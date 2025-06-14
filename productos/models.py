from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    foto_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre