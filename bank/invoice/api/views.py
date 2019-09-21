from django.db.models import Count, Q
from rest_framework import generics

from bank.invoice.api.filters import InvoiceFilter
from bank.invoice.api.serializers import InvoiceSerializer

from bank.invoice.models import Invoice
from rest_framework import filters as django_rest_filter
from django_filters.rest_framework import DjangoFilterBackend


class InvoiceListApi(generics.ListAPIView):
    serializer_class = InvoiceSerializer
    filter_class = InvoiceFilter
    filter_backends = (django_rest_filter.OrderingFilter, DjangoFilterBackend)
    ordering_fields = (
        "status",
        "amount",
        "due_date",
        "debtor__email"
    )

    def get_queryset(self):
        return Invoice.objects.all()
