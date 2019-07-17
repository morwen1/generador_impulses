from django.db import models
# Models
from django.contrib.auth.models import User


class Telefono(models.Model):
    numero = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.numero)


class Persona(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250, null=True, blank=True)
    cedula = models.CharField(max_length=250)
    genero = models.CharField(max_length=1)
    email = models.EmailField()
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefonos = models.ManyToManyField(Telefono, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.apellido:
            return '{} {}'.format(self.nombre, self.apellido)
        return '{}'.format(self.nombre)


class Administrador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.usuario)


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(User, related_name='usuarios', blank=True)

    def __str__(self):
        return '{}'.format(self.usuario)


class Analista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.usuario)


class Profesional(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.usuario)
