from django.db import models

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=50, verbose_name='Nombre')
    
    def __str__(self):
        return self.nombre_servicio
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = "Servicios"
        db_table = "servicio"
        ordering = ['id']
        

class Cita(models.Model):
    nombre_persona = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.CharField(max_length = 100, verbose_name='Email')
    telefono = models.IntegerField(verbose_name='Telefono')
    fecha_cita = models.DateField(verbose_name='Fecha')
    hora_cita = models.TimeField(verbose_name='Hora')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nombre_persona
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = "Citas"
        db_table = "citas"
        ordering = ['id']