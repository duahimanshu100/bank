from django.db import models

# Create your models here.
from bank.bank_account.models import Account
from bank.users.models import User


class Debtor(models.Model):
    first_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
