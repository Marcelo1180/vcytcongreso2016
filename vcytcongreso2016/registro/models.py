from django.db import models

# Create your models here.
#def inscripcion(model):
class Investigador(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    def __str__(self):
		return self.nombres