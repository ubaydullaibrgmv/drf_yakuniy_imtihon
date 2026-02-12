from rest_framework import serializers
from .models import Transaction
from .services import get_cbu_rates
from decimal import Decimal


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        wallet = validated_data['wallet']
        amount = validated_data['amount']
        to_wallet = validated_data.get('to_wallet')
        category = validated_data.get('category')

        rates_raw = get_cbu_rates()
        rates = {k: Decimal(str(v)) for k, v in rates_raw.items()}

        if to_wallet:
            if wallet.balance < amount:
                raise serializers.ValidationError("Mablag' yetarli emas!")

            amount_in_uzs = amount * rates[wallet.currency]
            final_amount = amount_in_uzs / rates[to_wallet.currency]

            wallet.balance -= amount
            to_wallet.balance += final_amount

            wallet.save()
            to_wallet.save()

        elif category:
            if category.type == 'expense':
                if wallet.balance < amount:
                    raise serializers.ValidationError("Balansda yetarli mablag' yo'q!")
                wallet.balance -= amount
            else:
                wallet.balance += amount
            wallet.save()

        return super().create(validated_data)