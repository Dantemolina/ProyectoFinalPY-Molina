from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.DecimalField(max_digits=20, decimal_places=0)
    ciudad_origen_id = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True)

