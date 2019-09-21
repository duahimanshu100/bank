from django.urls import path
from bank.invoice.api.views import InvoiceListApi

urlpatterns = [
    path('', InvoiceListApi.as_view(), name='api-invoice-list'),

]
