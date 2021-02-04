from rest_framework import serializers

from .models import PaymentMethod, CallBack


class PaymentMethodSerializer(serializers.ModelSerializer):
    """Способы оплаты"""
    class Meta:
        model = PaymentMethod
        exclude = ('order',)


class CallBackCreateSerializer(serializers.ModelSerializer):
    """Обратный звонок +"""
    class Meta:
        model = CallBack
        fields = ('__all__')
