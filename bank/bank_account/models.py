import uuid

from django.db import models


# Create your models here.
class Account(models.Model):
    iban = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
