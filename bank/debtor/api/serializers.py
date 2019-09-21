from rest_framework import serializers

from bank.bank_account.models import Account
from bank.debtor.models import Debtor


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['iban', ]


class DebtorSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    open_invoice = serializers.IntegerField()
    paid_invoice = serializers.IntegerField()
    overdue_invoice = serializers.IntegerField()
    canceled_invoice = serializers.IntegerField()

    class Meta:
        model = Debtor
        fields = ['id', 'email',
                  'account',
                  'open_invoice', 'paid_invoice', 'overdue_invoice', 'canceled_invoice']


class DebtorSerializerOnlyEmail(serializers.ModelSerializer):
    class Meta:
        model = Debtor
        fields = ['email', ]
