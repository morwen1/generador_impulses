# Generated by Django 2.1 on 2018-08-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capitulo', '0008_auto_20180820_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipopregunta',
            name='tipo',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
