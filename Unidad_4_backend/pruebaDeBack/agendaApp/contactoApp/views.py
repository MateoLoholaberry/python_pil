# Rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Models imports
from contactoApp.models import Contacto

# Serializers
from contactoApp.serializers import ContactoSerializer

# Helpers
from contactoApp.helpers.contactoError import contactoExiste

# Create your views here.
class ListaContactosApiView(APIView):
    
    def get(self, request):
        """get Retorna un listado de todos los contactos almacenados
        """
        
        contactos = Contacto.objects.all()
        
        contactos_serializados = ContactoSerializer(contactos, many=True)


        return Response(
            data=contactos_serializados.data,
            status=status.HTTP_200_OK
        )


class AgregarContactoApiView(APIView):

    def post(self, request):

        serializer = ContactoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            data = {
                'mensaje': 'El contacto se añadió correctamente'
            }

            return Response(
                data=data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class ModificarContactoApiView(APIView):
    
    def get(self, request, pk):
        
        validacion, contacto = contactoExiste(pk)
        
        if validacion:
            contacto_serializado = ContactoSerializer(contacto)
            
            return Response(
                data=contacto_serializado.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data=contacto,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    
    def put(self, request, pk):
        validacion, contacto = contactoExiste(pk)
        
        if validacion:
            contacto_serializado = ContactoSerializer(contacto, data=request.data)
        
            if contacto_serializado.is_valid():
                contacto_serializado.save()
                
                data = {
                    'mensaje':'El contacto se modificó correctamente'
                }
                
                return Response(
                    data=data,
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    data=contacto_serializado.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                data=contacto,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    
    def delete(self, request, pk):
        validacion, contacto = contactoExiste(pk)
        
        if validacion:
            contacto.delete()

            data = {
                'mensaje': 'El contacto se eliminó correctamente'
            }
            
            return Response(
                data=data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data=contacto,
                status=status.HTTP_400_BAD_REQUEST
            )