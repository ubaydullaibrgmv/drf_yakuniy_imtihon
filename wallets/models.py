from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Wallet(models.Model):

    TYPE_CHOICES = (
        ("cash", "Cash"),
        ("card", "Card"),
    )

    CURRENCY_CHOICES = (
        ("UZS", "UZS"),
        ("USD", "USD"),
        ("EUR", "EUR"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="wallets"
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.currency}"
