# Rest imports
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response



# Serializers imports
from apps.transaction.api.serializers import (
    TransactionSerializer,
    TransactionListSerializer
)


# Models imports
from apps.transaction.models import Transaction
from apps.account.models import Account


# Views
@api_view(['GET'])
def transaction_api_view(request):

    if request.method == 'GET':
        transaction = Transaction.objects.all().values('id', 'date', 'amount', 'operation_type')
        transaction_serializer = TransactionListSerializer(transaction, many=True)

        return Response(data=transaction_serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def transaction_detail_view(request, pk):
    """
    Detallar la operacion
    """

    # Validacion
    try:
        transaction = Transaction.objects.get(id=pk)

    except:
        return Response(
            {'message': 'Cuenta no encontrada'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail
    if request.method == 'GET':
        account_serializer = TransactionSerializer(transaction)

        return Response(account_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def deposit_api_view(request):

    if request.method == 'POST':
       
        transaction_serializer = TransactionSerializer(data=request.data)

        # Validación
        if transaction_serializer.is_valid():

            account = Account.objects.get(id=request.data['credit_account'])
            account.amount = account.amount + request.data['amount']
            
            account.save()
            transaction_serializer.save()

            return Response(data=transaction_serializer.data, status=status.HTTP_201_CREATED)

        return Response(transaction_serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def extraction_api_view(request):

    if request.method == 'POST':
       
        transaction_serializer = TransactionSerializer(data=request.data)

        # Validación de datos
        if transaction_serializer.is_valid():

            account = Account.objects.get(id=request.data['debit_account'])

            if account.amount - request.data['amount'] < 0:
                data = {
                    'message': 'No tiene fondos suficientes'
                }
                return Response(data=data, status=status.HTTP_406_NOT_ACCEPTABLE)

            account.amount = account.amount - request.data['amount']
            account.save()
            transaction_serializer.save()

            return Response(data=transaction_serializer.data, status=status.HTTP_201_CREATED)

        return Response(transaction_serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def transfer_api_view(request):

    if request.method == 'POST':
       
        transaction_serializer = TransactionSerializer(data=request.data)

        # Validación
        if transaction_serializer.is_valid():

            debit_account = Account.objects.get(id=request.data['debit_account'])
            credit_account = Account.objects.get(id=request.data['credit_account'])

            if debit_account.amount - request.data['amount'] < 0:
                data = {
                    'message': 'No tiene fondos suficientes'
                }
                return Response(data=data, status=status.HTTP_406_NOT_ACCEPTABLE)

            debit_account.amount = debit_account.amount - request.data['amount']
            debit_account.save()

            credit_account.amount = credit_account.amount + request.data['amount']
            credit_account.save()

            transaction_serializer.save()
            return Response(data=transaction_serializer.data, status=status.HTTP_201_CREATED)

        return Response(transaction_serializer.errors)