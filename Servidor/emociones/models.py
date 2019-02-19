#-*- coding: utf-8 -*-
from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Modelo que utilizara el servicio web
class Palabra(models.Model):
    """
    Los campos que tiene el modelo son: la palabra en sí y el grado de certeza, de 100 a 500, con el
    que se puede afirmar que una emoción la caracteriza expresados en porcentajes.
    """

    palabra = models.CharField(max_length=30)
    lexema = models.CharField(max_length=30)
    grados = models.CharField(validators=[validate_comma_separated_integer_list], max_length = 500)

    def __str__(self):
        return self.palabra

    class Meta:
        ordering = ('palabra',)
