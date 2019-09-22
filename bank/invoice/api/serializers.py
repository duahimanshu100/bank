from rest_framework import serializers

from bank.debtor.api.serializers import DebtorSerializerOnlyEmail
from bank.debtor.models import Debtor
from bank.invoice.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    debtor = DebtorSerializerOnlyEmail(many=False)
    custom_status = serializers.SerializerMethodField(source='get_custom_status')

    def get_custom_status(self, obj):
        return Invoice.STATUS_CHOICES[obj.status - 1]

    class Meta:
        model = Invoice
        fields = ['amount', 'due_date', 'debtor', 'custom_status']
