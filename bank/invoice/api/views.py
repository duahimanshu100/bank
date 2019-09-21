from django.db.models import Count, Q
from rest_framework import generics

from bank.invoice.api.serializers import InvoiceSerializer

from bank.invoice.models import Invoice


class InvoiceListApi(generics.ListAPIView):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.all()
            # .select_related('debtor_invoice')
