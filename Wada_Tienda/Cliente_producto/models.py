from django.db import models

class Cliente_producto(models.Model):
    cliente_id = models.ForeignKey(on_delete=models.SET_NULL, null=True, blank=True)
    producto_id = models.ForeignKey(on_delete=models.SET_NULL, null=True, blank=True)



class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
def __str__(self):
        return self.nombre












