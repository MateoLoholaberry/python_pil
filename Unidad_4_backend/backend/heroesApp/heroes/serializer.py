# Rest imports
from rest_framework import serializers

# Models
from heroes.models import Hero

# Serializer
class HeroSerializer(serializers.ModelSerializer):
    
    # Configuración principal
    class Meta:
        # Modelo que vamos a utilizar
        model = Hero
        # Campos que deseamos traducir (no necesariamente deben ser todos)
        fields = '__all__' # En este caso son todos los campos