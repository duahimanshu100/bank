from django.contrib import admin

# Register your models here.
from bank.invoice.models import Invoice

admin.site.register(Invoice)
