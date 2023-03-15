# Rest imports
from rest_framework import serializers


# Models imports
from apps.heroes.models import Hero


# Serializers
class HeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hero
        fields = '__all__'