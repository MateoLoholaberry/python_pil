# Rest imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


# Django imports
from django.contrib.sessions.models import Session


# Python imports
from datetime import datetime
import random


# Serializers imports
from apps.account.api.serializers import AccountSerializer
from apps.wallet.api.serializer import WalletSerializer
from apps.users.api.serializers import (
    UserSerializer,
    UserListSerializer,
    UserTokenSerializer
)


# Models imports
from apps.users.models import User
from apps.transaction.models import Transaction


# Views
@api_view(['GET', 'POST'])
def user_api_view(request):
    """
    Listar y crear usuarios.
    """

    # List
    if request.method == 'GET':

        users = User.objects.all().values('id', 'username', 'email', 'password')
        users_serializer = UserListSerializer(users, many=True)

        return Response(data=users_serializer.data,status=status.HTTP_200_OK)

    # Create
    elif request.method == 'POST':

        # User
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()

            # Account
            alias = str(user_serializer.data['username']) + '.wallet'

            data = {
                'user': user_serializer.data['id'],
                'account_number': random.randint(0, 100000),
                'alias': alias,
                'amount': 0
            }
            account_serializer = AccountSerializer(data=data)

            # Validación
            if account_serializer.is_valid():
                account_serializer.save()
            
                # Wallet
                data = {
                    'user': user_serializer.data['id'],
                    'account': account_serializer.data['id']
                }

                wallet_serializer = WalletSerializer(data=data)

                # Validación
                if wallet_serializer.is_valid():
                    wallet_serializer.save()

                    data = {
                        'user_id': user_serializer.data['id'],
                        'username': user_serializer.data['username'],
                        'account_id': account_serializer.data['id'],
                        'account_alias': account_serializer.data['alias'],
                        'wallet_id': wallet_serializer.data['id']
                    }

                    return Response(data=data, status=status.HTTP_201_CREATED)
                return Response(wallet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def user_detail_view(request, pk):
    """
    Detallar, actualizar y eliminar un usuario.
    """

    # Validacion
    try:
        user = User.objects.get(id=pk)

    except:
        return Response(
            {'message': 'Usuario no encontrado'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail
    if request.method == 'GET':
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data)

    # Update
    elif request.method == 'PUT':
        user_serializer = UserSerializer(user, data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()

            return Response(data=user_serializer.data)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete
    elif request.method == 'DELETE':
        user.delete()

        return Response(
            {'message': 'Usuario eliminado correctamente'},
            status=status.HTTP_200_OK
        )


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        print(request.data)
        login_serializer = self.serializer_class(data=request.data, context = {'request':request})
        if login_serializer.is_valid():
            
            user = login_serializer.validated_data['user']

            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)

                if created:
                    return Response(
                        {'token': token.key,
                        'user': user_serializer.data
                        },
                        status=status.HTTP_200_OK
                    )
                
                else:
                    token.delete()
                    token = Token.objects.create(user=user)

                    return Response(
                        {'token': token.key,
                        'user': user_serializer.data
                        },
                        status=status.HTTP_200_OK
                    )

            else:
                return Response(
                    {'error': 'Este usuario no puede iniciar sesión'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

        else:
            return Response(
                {'error': 'Username o password incorrectos'},
                status=status.HTTP_400_BAD_REQUEST
            )


class Logout(APIView):

    def post(self, request, *args, **kwargs):

        try:
            token = Token.objects.get(key=request.data['token'])
            
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())

                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                
                token.delete()

                return Response(
                    {'message': "Sesión finalizada"},
                    status=status.HTTP_200_OK
                )
            
            return Response(
                {'error': 'Token no encontrado'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        except:
            return Response(
                {'error': 'No se ha encontrado token en la peticion'},
                status=status.HTTP_409_CONFLICT
            )