from django.db import models
class aprendiz (models.Model):
    nombre  = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    documento = models.IntegerField(unique = True)
    correo = models.EmailField(unique = True)
    telefono = models.IntegerField(unique=True)
    ficha = models.IntegerField()
    programa = models.CharField(max_length = 50)

    def __str__ (self):
        return f'{self.nombre}'

# Create your models here.
