from django.db import models
from datetime import datetime
# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def obtenerAnio(self):
        anioAct= datetime.now().year
        anio= anioAct - self.edad
        return anio
    def cedulaProvi(self):
        cedula = str(self.cedula).strip()
        codigo = cedula[:2]
    
        if codigo == "11":
            ciudad = "Loja"
            return ciudad
        else:
            ciudad= "Otra cedula"
            return ciudad
                
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} - CI: {self.cedulaProvi()} - Edad {self.edad} - Año de nacimiento: {self.obtenerAnio()}" 
     