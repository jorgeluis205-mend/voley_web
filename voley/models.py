from django.db import models

class Persona(models.Model):
    id_persona=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name=("Persona")
        verbose_name_plural=("1. Personas")
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Equipo(models.Model):
    id_equipo=models.AutoField(primary_key=True)
    equipo=models.CharField(max_length=50, null=False)
    personas=models.ManyToManyField(Persona, related_name="equipo")

    class Meta:
        verbose_name=("Equipo")
        verbose_name_plural=("2. Equipos")

    def __str__(self):
        return self.equipo
    
