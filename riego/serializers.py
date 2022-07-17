from rest_framework import serializers
from riego.models import riego_modelo

class riego_serializer(serializers.ModelSerializer):
    class Meta:
        model = riego_modelo
        fields = ('__all__')