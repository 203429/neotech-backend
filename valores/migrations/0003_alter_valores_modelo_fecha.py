# Generated by Django 4.0.6 on 2022-07-17 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valores', '0002_valores_modelo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valores_modelo',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 17, 13, 32, 23, 900333)),
        ),
    ]
