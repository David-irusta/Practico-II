from django.db import models

class Oficina(models.Model):
    nombre = models.CharField(verbose_name='Nombre de la oficina', max_length=100)
    nombre_corto = models.CharField(verbose_name='Nombre corto', max_length=50)

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'
        ordering = ['nombre']