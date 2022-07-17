from time import time
from django.conf import settings
from django.db import models
from django.utils import timezone

class valores_modelo(models.Model):
    temp_ambiente = models.FloatField(null=True)
    humedad_ambiente = models.FloatField(null=True)
    humedad_suelo = models.FloatField(null=True)
    nivel_agua = models.FloatField(null=True)
    fecha = models.DateTimeField(default=timezone.now)