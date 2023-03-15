from rest_framework import serializers
from django.db.models import Q

# Models imports
from apps.wallet.models import Wallet
from apps.transaction.models import Transaction

# Serializer imports
from apps.transaction.api.serializers import TransactionSerializer


# Serializers
class WalletSerializer(serializers.ModelSerializer):

    transaction = serializers.SerializerMethodField()


    class Meta:
        model = Wallet
        fields = (
            'id',
            'user',
            'account',
            'transaction'
        )
    
    def get_transaction(self, obj):
    
        transactions = Transaction.objects.filter(
            Q(credit_account=obj.account.id) | Q(debit_account=obj.account.id)
        )
        return TransactionSerializer(transactions, many=True, read_only=True).data


class WalletListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'user': instance['user']
        }