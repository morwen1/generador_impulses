# Generated by Django 2.1 on 2018-08-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capitulo', '0004_auto_20180818_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='nivel',
            field=models.IntegerField(default=0),
        ),
    ]
