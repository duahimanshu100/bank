from rest_framework import serializers

from bank.debtor.api.serializers import DebtorSerializerOnlyEmail
from bank.debtor.models import Debtor
from bank.invoice.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    debtor = DebtorSerializerOnlyEmail(many=False)

    class Meta:
        model = Invoice
        fields = ['amount', 'due_date', 'debtor']
