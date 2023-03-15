# Rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Models imports
from apps.heroes.models import Hero


# Serializers imports
from apps.heroes.api.serializers import HeroSerializer


# Create your views here.
class HeroApiView(APIView):

    def get(self, request):
        """Retorna un listado con todos los heroes almacenados en la base"""

        hero = Hero.objects.all()
        hero_serializer = HeroSerializer(hero, many=True)

        return Response(
            data=hero_serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """Crea un nuevo registro"""

        serializer = HeroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {'message': 'Heroe creado correctamente'},
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class HeroDetailApiView(APIView):

    def get(self, request, pk):
        """Retorna un listado con todos los heroes almacenados en la base"""

        hero = Hero.objects.get(pk=pk)
        hero_serializer = HeroSerializer(hero)

        return Response(
            data=hero_serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        """Modifica un registro"""

        hero = Hero.objects.get(pk=pk)
        serializer = HeroSerializer(hero, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {'message': 'Heroe modificado correctamente'},
                status=status.HTTP_200_OK
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """Modifica un registro"""

        hero = Hero.objects.get(pk=pk)
        hero.delete()

        return Response(
            {'message': 'Heroe eliminado correctamente'},
            status=status.HTTP_200_OK
        )