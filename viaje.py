from django.db import models
class viaje(models.Model):
    NombreViaje=models.AutoField(primary_key=true)
    DescripcionViaje=models.CharField(max_length=100)
    precioViaje=models.CharField(max_length=1000)
    ofertaViaje=models.CharField(max.length=100)

