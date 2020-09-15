from django.db import models
from django.utils import timezone


class Preguntas(models.Model):

    asignatura = models.CharField(max_length=50)
    pregunta = models.TextField()
    respuesta_a = models.TextField()
    respuesta_b = models.TextField()
    respuesta_c = models.TextField()
    respuesta_d = models.TextField()
    respuesta_correcta = models.CharField(max_length=1)
    aciertos = models.IntegerField(default=0)
    fallos = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(default=timezone.now)



