from django.db import models

class Tarea(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    fecha_cumplimiento = models.DateField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

