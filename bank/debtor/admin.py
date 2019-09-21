from django.contrib import admin

# Register your models here.
from bank.debtor.models import Debtor
from bank.invoice.models import Invoice


class InvoiceInline(admin.StackedInline):
    model = Invoice


class DebtorAdmin(admin.ModelAdmin):
    inlines = (InvoiceInline,)


admin.site.register(Debtor, DebtorAdmin)
