from rest_framework import serializers
from django.conf import settings

from .models import PaymentMethod, CallBack


class PaymentMethodSerializer(serializers.ModelSerializer):
    """Способы оплаты"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = PaymentMethod
        exclude = ('order',)


class CallBackCreateSerializer(serializers.ModelSerializer):
    """Обратный звонок +"""
    class Meta:
        model = CallBack
        fields = ('__all__')
