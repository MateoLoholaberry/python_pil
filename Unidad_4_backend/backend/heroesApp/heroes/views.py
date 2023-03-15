# Rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Models imports
from heroes.models import Hero

# Serializers imports
from heroes.serializer import HeroSerializer

# Helpers
from heroes.helpers import heroe_errors

# Create your views here.
class HeroApiView(APIView):

    def get(self, request):
        """get Retorna un listado con todos los heroes almacenados en la base
        """
        
        # print(f'REQUEST --> {request}')
        
        heroes = Hero.objects.all()
        # print(heroes)
        # print(heroes.values())
        
        heroes_serializer = HeroSerializer(heroes, many=True)
        # print(heroes_serializer)
        # print(heroes_serializer.data) # Esto ya me devuelve los datos serializados
        
        
        """ data = {
            'mensaje': 'Hola desde HeroApiView',
        } """
        
        return Response(
            data=heroes_serializer.data,
            status=status.HTTP_200_OK
        )
    
    
    def post(self, request):
        """post Crea un nuevo registro/heroe
        """
        print("Primer post")
        # print('ESTAMOS EN EL MÉTODO POST!!')
        # print(request.data)
        serializer = HeroSerializer(data=request.data)
        
        if serializer.is_valid(): # Comprueba que la información que pasamos sea valida, o sea cumpla con todos los requisitos de todas las propiedades que nosotros pusimos en el modelo.
            serializer.save()
        
            data = {
                'mensaje': 'El heroe se creó de forma correcta'
            }
            
            return Response(
                data=data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def hero_api_view(request):
    
    heroes = Hero.objects.all()
    heroes_serializer = HeroSerializer(heroes, many=True)
    
    return Response(
        data=heroes_serializer.data,
        status=status.HTTP_200_OK
    )


# Vista independiente para el método post, en vez de usar la misma vista que el get
class CreateHeroApiView(APIView):
    def post(self, request):
        """post Crea un nuevo registro/heroe
        """
        print("Otro post")
        # print('ESTAMOS EN EL MÉTODO POST!!')
        # print(request.data)
        serializer = HeroSerializer(data=request.data)

        if serializer.is_valid(): # Comprueba que la información que pasamos sea valida, o sea cumpla con todos los requisitos de todas las propiedades que nosotros pusimos en el modelo.
            serializer.save()
        
            data = {
                'mensaje': 'El heroe se creó de forma correcta'
            }
            
            return Response(
                data=data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class HeroDetailApiView(APIView):
    def get(self, request, pk):
        """get Nos devuelve más información de un heroe particular
        """
        # 1° opción
        # heroe = Hero.objects.filter()

        # 2° opción
        try:
            # el método get devuelve un error por lo tanto hay que ponerlo dentro de un try except para que no corte el flujo del programa.
            heroe = Hero.objects.get(pk=pk)
        except:
            data = {
                'menaje':'El el objeto que se pasó por parametro no existe'
            }
            return Response(
                data=data,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        heroe_serializer = HeroSerializer(heroe)
        
        return Response(
            data=heroe_serializer.data,
            status=status.HTTP_200_OK
        )


    def put(self, request, pk):
        """put Modifica un registro
        """
        validacion, heroe = heroe_errors.hayHeroe(pk)

        # 2° opción
        # heroe = Hero.objects.get(pk=pk)
        
        if validacion:
            heroe_serializer = HeroSerializer(heroe, data=request.data)
        
            if heroe_serializer.is_valid():
                heroe_serializer.save()
            
                data = {
                    'mensaje': 'El heroe se modificó de forma correcta'
                }
            
                return Response(
                    data=data,
                    status=status.HTTP_200_OK
                )
        
            return Response(
                data=heroe_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                data=heroe,
                status=status.HTTP_400_BAD_REQUEST
            )


    def delete(self, request, pk):
        """delete elimina un registro"""
        
        # heroe = Hero.objects.get(pk=pk)
        
        validacion, heroe = heroe_errors.hayHeroe(pk)
        
        if validacion:
            heroe.delete()
            
            data = {
                'mensaje': 'El heroe se eliminó de forma correcta'
            }
            
            return Response(
                data=data,
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                data=heroe,
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET', 'PUT', 'DELETE'])
def hero_detail__api_view(request, pk):

    # Detail
    if request.method == 'GET':
        validacion, heroe = heroe_errors.hayHeroe(pk)

        if validacion:
            heroe_serializer = HeroSerializer(heroe)

            return Response(
                data=heroe_serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            data=heroe,
            status=status.HTTP_400_BAD_REQUEST
        )


    # Update
    elif request.method == 'PUT':

        # heroe = Hero.objects.get(pk=pk)

        validacion, heroe = heroe_errors.hayHeroe(pk)

        if validacion:
            heroe_serializer = HeroSerializer(heroe, data=request.data)

            if heroe_serializer.is_valid():
                heroe_serializer.save()

                data = {
                    'mensaje': 'El heroe se modificó de forma correcta'
                }

                return Response(
                    data=data,
                    status=status.HTTP_200_OK
                )

            return Response(
                data=heroe_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                data=heroe,
                status=status.HTTP_400_BAD_REQUEST
            )


    # Delete
    elif request.method == 'DELETE':
        # heroe = Hero.objects.get(pk=pk)

        validacion, heroe = heroe_errors.hayHeroe(pk)

        if validacion:
            heroe.delete()

            data = {
                'mensaje': 'El heroe se eliminó de forma correcta'
            }

            return Response(
                data=data,
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                data=heroe,
                status=status.HTTP_400_BAD_REQUEST
            )