from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from bank.bank_account.models import Account
from bank.debtor.models import Debtor


class DebtorList(LoginRequiredMixin, ListView):
    model = Debtor

    def get_queryset(self):
        owner = self.request.user
        from bank.invoice.models import Invoice
        return self.model.objects.filter(owner=owner) \
            .annotate(
            open_invoice=Count('debtor_invoice__status', filter=Q(debtor_invoice__status=Invoice.OPEN))) \
            .annotate(
            paid_invoice=Count('debtor_invoice__status', filter=Q(debtor_invoice__status=Invoice.PAID))) \
            .annotate(
            canceled_invoice=Count('debtor_invoice__status', filter=Q(debtor_invoice__status=Invoice.CANCELED)))\
            .annotate(
            overdue_invoice=Count('debtor_invoice__status', filter=Q(debtor_invoice__status=Invoice.OVERDUE)))


class DebtorUpdateView(LoginRequiredMixin, UpdateView):
    model = Debtor
    fields = ['first_name', 'last_name', 'email', ]
    success_url = reverse_lazy('debtor-list')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(owner=owner)


class DebtorCreate(LoginRequiredMixin, CreateView):
    model = Debtor
    fields = ['first_name', 'last_name', 'email', ]

    success_url = reverse_lazy('debtor-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.account = Account.objects.create()
        return super(DebtorCreate, self).form_valid(form)

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(owner=owner)


class DebtorDeleteView(DeleteView):
    model = Debtor
    success_url = reverse_lazy('debtor-list')
