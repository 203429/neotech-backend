from django.db import models
from django.utils import timezone

class riego_modelo(models.Model):
    tipo = models.CharField(null=False, max_length=20)
    fecha = models.DateTimeField(default=timezone.now)