import django_filters
from django.db.models import Count, Q

from bank.debtor.models import Debtor
from django_filters import rest_framework as filters

from bank.invoice.models import Invoice


class InvoiceFilter(filters.FilterSet):
    email = django_filters.CharFilter(method="filter_email", label='Email')

    class Meta:
        model = Invoice
        fields = ["status", "amount", "due_date", "email"]

    def filter_email(self, queryset, name, value):
        return queryset.filter(debtor__email=value)
