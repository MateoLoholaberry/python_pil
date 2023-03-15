# Rest imports
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response



# Serializers imports
from apps.account.api.serializers import (
    AccountSerializer,
    AccountListSerializer
)


# Models imports
from apps.account.models import Account


# Views
@api_view(['GET'])
def account_api_view(request):

    # List
    if request.method == 'GET':
        account = Account.objects.all().values('id', 'user', 'account_number', 'alias')
        account_serializer = AccountListSerializer(account, many=True)

        return Response(data=account_serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def account_detail_view(request, pk):
    """
    Detallar una cuenta
    """

    # Validacion
    try:
        account = Account.objects.get(id=pk)

    except:
        return Response(
            {'message': 'Cuenta no encontrada'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail
    if request.method == 'GET':
        account_serializer = AccountSerializer(account)

        return Response(account_serializer.data)