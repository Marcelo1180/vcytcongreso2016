#!/usr/bin/python
# -*- coding: utf8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
# from django import forms

# Create your models here.
# class Departamento(models.Model):
YEAR_CHOICES = []
for y in range(1980, 2015):
    YEAR_CHOICES.append((y, y))

GENERO_CHOICES = (
    ('F', 'Femenino'),
    ('M', 'Masculino'),
)

def validate_cant_year(value):
    if value>1 and value<100:
        raise ValidationError('%s some error message' % value)

class Pais(models.Model):
    pais = models.CharField(max_length=50)
    def __str__(self):
		return self.pais

class Frascati_nivel(models.Model):
    frascati_nivel = models.CharField(max_length=50)

class Frascati_categoria(models.Model):
    frascati_categoria = models.CharField(max_length=50)

class Departamento(models.Model):
    departamento = models.CharField(max_length=50)

#def inscripcion(model):
class Investigador(models.Model):
    # DATOS PERSONALES
    nombre_completo = models.CharField(max_length=100, verbose_name='Nombre y Apellidos')
    pasaporte = models.CharField(max_length=50)
    lugar_nacimiento = models.CharField(max_length=100, verbose_name='Lugar de nacimiento')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    telefono = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    email = models.EmailField(verbose_name='Email personal')
    email_institucional = models.EmailField(default='', verbose_name='Email institucional')
    nacionalidad_origen = models.ForeignKey(Pais, related_name='nacionalidad_origen', verbose_name='Nacionalidad de origen', help_text='Nacionalidad Actual donde reside')
    nacionalidad_actual = models.ForeignKey(Pais, related_name='nacionalidad_actual', verbose_name='Nacionalidad actual')
    foto = models.ImageField(upload_to='uploads/foto', verbose_name='Fotografia 3x3(cm)')
    # FORMACION
    profesion = models.CharField(max_length=100)
    max_grado = models.CharField(max_length=50, verbose_name='Maximo grado academico')
    max_grado_upload = models.FileField(upload_to='uploads/max_grado', verbose_name='Adjuntar copia digital del titulo')
    max_grado_year = models.IntegerField(choices=YEAR_CHOICES, verbose_name='Año de obtencion')
    universidad_profesion = models.CharField(max_length=100)
    universidad_postgrado = models.CharField(max_length=100)
    # DATOS LABORALES
    institucion = models.CharField(max_length=50, verbose_name='Institucion')
    institucion_ciudad = models.CharField(max_length=50, verbose_name='Ciudad')
    institucion_pais = models.ForeignKey(Pais, related_name='Pais')
    frascati_nivel = models.ForeignKey(Frascati_nivel, verbose_name='Area de investigacion')
    frascati_categoria = ChainedForeignKey(Frascati_categoria, chained_field='frascati_nivel', chained_model_field='frascati_nivel', verbose_name='Area de investigacion')
    especialidad = models.CharField(max_length=150)
    experiencia_year = models.IntegerField(validators=[validate_cant_year], verbose_name='Años de experiencia')
    curriculum = models.FileField(upload_to='uploads/curriculum', verbose_name='Curriculum Vitae')
    # PUBLICACIONES
    publicacion = models.CharField(max_length=50, verbose_name='Colocar el enlace')
    # DISPONIBILIDAD DE TIEMPO PARA ASISTIR CONGRESO
    pais_origen = models.ForeignKey(Pais, related_name='pais_origen', verbose_name='País de origen')
    ciudad_origen = models.CharField(max_length=100, verbose_name='Ciudad de origen')
    aeropuerto_origen = models.CharField(max_length=100, verbose_name='Aeropuerto de origen')
    fecha_llegada = models.DateField(verbose_name='Fecha de llegada a Bolivia(Cochabamba)')
    fecha_retorno = models.DateField(verbose_name='Fecha de retorno')
    comment = models.TextField(verbose_name='Comentarios')
    # def save(self, *args, **kwargs):
    #     if self.image:
    #         self.image = get_thumbnail(self.image, '115x115', quality=80, format='JPEG')
    #     super(MyPhoto, self).save(*args, **kwargs)

    def __str__(self):
		return self.nombres