from django.db import models

# Create your models here.
class sexo(models.Model):
	sexo =models.CharField(max_length=10)

	def __str__(self):
		return self.sexo

class alumno(models.Model):
	Identidad=models.CharField(max_length=15)
	nombres =models.CharField(max_length=50)
	apellidos =models.CharField(max_length=50)
	fechaNac = models.DateField()
	sexo =models.ForeignKey(sexo, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{} {} {}'.format(self.Identidad, self.nombres, self.apellidos)

