import django_filters
from django.db.models import Count, Q

from bank.debtor.models import Debtor
from django_filters import rest_framework as filters


class DebtorFilter(filters.FilterSet):
    invoice_status = django_filters.NumberFilter(method="filter_invoice_status")
    invoice_count = django_filters.NumberFilter(method="filter_invoice_count")

    class Meta:
        model = Debtor
        fields = ["invoice_status", "invoice_count"]

    def filter_invoice_status(self, queryset, name, value):
        return queryset.filter(debtor_invoice__status=value)

    def filter_invoice_count(self, queryset, name, value):
        return queryset.annotate(invoice_count=Count('debtor_invoice')).filter(invoice_count=value)
