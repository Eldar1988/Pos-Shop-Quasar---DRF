from rest_framework import serializers
from .models import MainColor, Script, ProductCardSettings


class MainColorSerializer(serializers.ModelSerializer):
    """Основные цвета магазаина"""

    class Meta:
        model = MainColor
        fields = '__all__'


class ScriptSerializer(serializers.ModelSerializer):
    """Скрипты для сайта"""

    class Meta:
        model = Script
        fields = '__all__'


class ProductCardSettingsSerializer(serializers.ModelSerializer):
    """Настройки карточки товара"""

    class Meta:
        model = ProductCardSettings
        fields = '__all__'

