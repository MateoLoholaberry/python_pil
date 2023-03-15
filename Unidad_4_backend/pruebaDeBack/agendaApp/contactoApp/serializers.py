# Rest imports
from rest_framework import serializers

# Models imports
from contactoApp.models import Contacto

class ContactoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacto
        fields = '__all__'
