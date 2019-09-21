from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, UpdateView, CreateView

from bank.bank_account.models import Account
from bank.debtor.models import Debtor


class DebtorList(LoginRequiredMixin, ListView):
    model = Debtor

    def get_queryset(self):
        return Debtor.objects.filter(owner=self.request.user)


class DebtorUpdateView(LoginRequiredMixin, UpdateView):
    model = Debtor
    fields = ['first_name', 'last_name', 'email', ]

    def get_success_url(self):
        return '/debtors'


class DebtorCreate(LoginRequiredMixin, CreateView):
    model = Debtor
    fields = ['first_name', 'last_name', 'email', ]

    def get_success_url(self):
        return '/debtors'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.account = Account.objects.create()
        # account =
        return super(DebtorCreate, self).form_valid(form)
