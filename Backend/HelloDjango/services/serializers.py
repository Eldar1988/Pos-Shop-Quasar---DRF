from rest_framework import serializers

from .models import Category, Service, Image


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'slug')


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service