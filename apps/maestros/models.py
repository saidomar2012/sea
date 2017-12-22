from django.db import models

from apps.alumno.models import sexo

class maestros(models.Model):
	Identidad=models.CharField(max_length=15)
	nombres =models.CharField(max_length=50)
	apellidos =models.CharField(max_length=50)
	fechaNac = models.DateField()
	sexo =models.ForeignKey(sexo, null=True, blank=True, on_delete=models.CASCADE)

# Create your models here.
