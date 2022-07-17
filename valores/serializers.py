from dataclasses import fields
from rest_framework import serializers
from valores.models import valores_modelo

class valores_serializer(serializers.ModelSerializer):
    class Meta:
        model = valores_modelo
        fields = ('__all__')

class valores_ambiente_serializer(serializers.ModelSerializer):
    class Meta:
        model = valores_modelo
        fields = ('temp_ambiente','humedad_ambiente','fecha')

class valores_suelo_serializer(serializers.ModelSerializer):
    class Meta:
        model = valores_modelo
        fields = ('humedad_suelo','fecha')

class valores_agua_serializer(serializers.ModelSerializer):
    class Meta:
        model = valores_modelo
        fields = ('nivel_agua','fecha')