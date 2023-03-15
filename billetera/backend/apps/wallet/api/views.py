# Rest imports
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response



# Serializers imports
from apps.wallet.api.serializer import (
    WalletSerializer,
    WalletListSerializer
)


# Models imports
from apps.wallet.models import Wallet


# Views
@api_view(['GET'])
def wallet_api_view(request):

    # List
    if request.method == 'GET':
        wallet = Wallet.objects.all().values('id', 'user')
        wallet_serializer = WalletListSerializer(wallet, many=True)

        return Response(data=wallet_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def wallet_detail_view(request, pk):
    """
    Detallar la operacion
    """

    # Validacion
    try:
        wallet = Wallet.objects.get(id=pk)

    except:
        return Response(
            {'message': 'Wallet no encontrada'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail
    if request.method == 'GET':
        wallet_serializer = WalletSerializer(wallet)

        return Response(wallet_serializer.data)
    
    # Delete
    elif request.method == 'DELETE':
        wallet.delete()

        return Response(
            {'message': 'Cuenta eliminada correctamente'},
            status=status.HTTP_200_OK
        )
