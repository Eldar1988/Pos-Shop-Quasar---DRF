from rest_framework import serializers

from .models import PaymentMethod


class PaymentMethodSerializer(serializers.ModelSerializer):
    """Способы оплаты"""
    class Meta:
        model = PaymentMethod
        exclude = ('order',)