from django.db import models

# Create your models here.
from bank.debtor.models import Debtor


class Invoice(models.Model):
    OPEN = 1
    PAID = 2
    OVERDUE = 3
    CANCELED = 4
    STATUS_CHOICES = [
        (OPEN, 'OPEN'),
        (PAID, 'PAID'),
        (OVERDUE, 'OVERDUE'),
        (CANCELED, 'CANCELED'),
    ]
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=OPEN,
    )
    amount = models.FloatField()
    due_date = models.DateField()
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE, related_name='debtor_invoice')

    def __str__(self):
        return str(self.amount) + '-->' + str(self.status)
