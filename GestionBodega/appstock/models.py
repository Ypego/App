from django.db import models

class productos(models.Model):
    cod_prod=models.IntegerField()
    cant_prod=models.IntegerField()
    nombre_prod=models.CharField(max_length=25)
    tipo_prod=models.CharField(max_length=20)
