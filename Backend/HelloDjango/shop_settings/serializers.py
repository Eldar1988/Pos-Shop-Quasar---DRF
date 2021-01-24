from rest_framework import serializers
from .models import MainColor, Script


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
