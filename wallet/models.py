import uuid
from decimal import Decimal
from django.db import models
from django.conf import settings


class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    account_number = models.CharField(max_length=11, unique=True)

    def deposit(self, amount):
        if amount > Decimal('0.00'):
            self.balance += amount
        return False




class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("D", "Deposit"),
        ("W", "Withdraw"),
        ("T", "Transfer"),
    ]
    amount  = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    reference = models.CharField(max_length=255, default='ref_' + str(uuid.uuid4))
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPES, default='D')
    transaction_time = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver', null=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender', null=True)
