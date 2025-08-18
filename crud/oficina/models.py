from django.db import models
from django.core.exceptions import ValidationError

def validate_nombre_corto(value):
    if not value.isupper():
        raise ValidationError("El nombre corto debe ser en mayuscula")

class Oficina(models.Model):
    nombre = models.CharField(verbose_name='Nombre de la oficina', max_length=50, unique=True)
    nombre_corto = models.SlugField(verbose_name='Id corto', max_length=10, unique=True, help_text='Codigo corto unico (ej, PER, ADM, etc)')
    validators = [validate_nombre_corto]

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    def __str__(self):
        """Unicode representation of Oficina"""
        return f"{self.nombre} ({self.nombre_corto})"