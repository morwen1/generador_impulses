from django.db import models


class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    analistas = models.IntegerField()
    profesionales_min = models.IntegerField()
    profesionales_max = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)


class Licencia(models.Model):
    analistas = models.IntegerField()
    profesionales = models.IntegerField()
    duracion = models.IntegerField()
    fecha_vencimiento = models.DateField()

    @property
    def licencias_cliente(self):
        return self.licenciacliente_set.all()

    class Meta:
        db_table = 'licencia'


class LicenciaCliente(models.Model):
    licencia = models.ForeignKey(Licencia, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    cliente = models.ForeignKey('user.Cliente', on_delete=models.CASCADE)
    norma = models.ForeignKey('norma.Norma', on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.cliente, self.cliente, self.norma)

    class Meta:
        db_table = 'licencia_cliente'
