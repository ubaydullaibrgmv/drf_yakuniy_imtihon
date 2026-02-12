from django.db import models
from wallets.models import Wallet
from categories.models import Category


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactions")
    to_wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name="transfers_received")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)