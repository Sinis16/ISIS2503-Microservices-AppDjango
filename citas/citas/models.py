from django.db import models

class Cita(models.Model):
    paciente = models.IntegerField(null=False, default=None)
    fecha = models.CharField(max_length=50)
    hora_inicio = models.CharField(max_length=50)
    hora_fin = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)