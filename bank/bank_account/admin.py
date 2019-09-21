from django.contrib import admin

# Register your models here.
from bank.bank_account.models import Account

admin.site.register(Account)
