# Generated by Django 4.0.6 on 2022-07-17 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='valores_modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_ambiente', models.FloatField(null=True)),
                ('humedad_ambiente', models.FloatField(null=True)),
                ('humedad_suelo', models.FloatField(null=True)),
                ('nivel_agua', models.FloatField(null=True)),
            ],
        ),
    ]
