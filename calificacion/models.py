from django.db import models
from django.contrib.auth.models import User

class Calificacion(models.Model):
    contenido = models.CharField(max_length=150, verbose_name="Comentario")
    puntuacion = models.IntegerField(verbose_name="Calificacion")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.contenido
    
    class Main:
        verbose_name = "Calificacion"
        verbose_name_plural = "Calificaciones"
        db_table = "calificaciones"
        ordering = ['id']
    