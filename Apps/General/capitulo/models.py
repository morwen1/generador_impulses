from django.db import models


class Capitulo(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    ponderacion = models.IntegerField(null=True)
    norma = models.ForeignKey('norma.Norma', null=True, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    @property
    def preguntas(self):
        return self.pregunta_set.all()

    class Meta:
        db_table = 'capitulo'


class TipoPregunta(models.Model):
    tipo = models.CharField(max_length=250, unique=True)
    esp = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.esp)

    class Meta:
        db_table = 'capitulo_tipo_pregunta'


class Pregunta(models.Model):
    descripcion = models.TextField()
    nivel = models.IntegerField(default=0)
    ponderacion = models.IntegerField(null=True)
    sugerencia = models.TextField()
    tipo = models.ForeignKey(TipoPregunta, on_delete=models.CASCADE)
    capitulo = models.ForeignKey(Capitulo, null=True, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)

    @property
    def tipo_pregunta(self):
        return self.tipo.tipo

    def __str__(self):
        return '{}'.format(self.descripcion)
