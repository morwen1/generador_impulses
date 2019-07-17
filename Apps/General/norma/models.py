from django.db import models


class Norma(models.Model):
    descripcion = models.CharField(max_length=250)
    ponderada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)

    @property
    def tipo_norma(self):
        if self.ponderada:
            return 'Ponderada'
        return 'No Ponderada'

    @property
    def capitulos(self):
        return self.capitulo_set.all()

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        db_table = 'norma'
