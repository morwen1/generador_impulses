# Generated by Django 2.1 on 2018-08-18 22:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('capitulo', '0006_auto_20180818_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregunta',
            name='fecha_edicion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tipopregunta',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipopregunta',
            name='fecha_edicion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]