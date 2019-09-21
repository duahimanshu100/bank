from django.db.models import Count, Q
from rest_framework import generics

from bank.debtor.api.serializers import DebtorSerializer
from bank.debtor.models import Debtor
from bank.invoice.models import Invoice


class DebtorListApi(generics.ListAPIView):
    serializer_class = DebtorSerializer

    def get_queryset(self):
        return Debtor.objects.annotate(
            open_invoice=Count('debtor_invoice__status', filter=Q(debtor_invoice__status=Invoice.OPEN))) \
            .annotate(
            paid_invoice=Count('debtor_invoice__status', filter=Q(debtor_invoice__status=Invoice.PAID))) \
            .annotate(
            canceled_invoice=Count('debtor_invoice__status', filter=Q(debtor_invoice__status=Invoice.CANCELED))) \
            .annotate(
            overdue_invoice=Count('debtor_invoice__status', filter=Q(debtor_invoice__status=Invoice.OVERDUE)))
