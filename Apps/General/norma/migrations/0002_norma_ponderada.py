# Generated by Django 2.1 on 2018-08-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='norma',
            name='ponderada',
            field=models.BooleanField(default=False),
        ),
    ]
