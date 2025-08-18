from django.db import models
from oficina.models import Oficina

class Persona(models.Model):
    apellido = models.CharField(verbose_name='Apellido', max_length=50)
    nombre = models.CharField(verbose_name='Nombre Completo', max_length=100)
    edad = models.IntegerField(verbose_name='Edad')
    oficina = models.ForeignKey(Oficina, 
    verbose_name= 'Oficina asignada', on_delete= models.PROTECT, related_name= "personas", null= True, blank = True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.apellido}, {self.nombre} - Oficina: {self.oficina.nombre}'



