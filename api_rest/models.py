from django.db import models

# Create your models here.
class Refresco(models.Model):
    nombre=models.CharField(max_length=30)
    sabor=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    presentacion=models.CharField(max_length=30,choices=[("Botella", "Botella"), ("Lata", "Lata"), ("Botella Mini", "Botella Mini")])
    fecha_creado=models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return f"{self.nombre}-{self.sabor}-{self.marca}-{self.fecha_creado}"