# Generated by Django 2.1 on 2018-08-24 03:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180823_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_edicion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
