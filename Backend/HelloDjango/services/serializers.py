from rest_framework import serializers

from .models import Category, Service, Image, ServiceRequest


class ServiceCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'slug')


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'miniature')


class ServiceCategoryDetailSerializer(serializers.ModelSerializer):
    services = ServiceListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        exclude = ('pub_date', 'update', 'order', 'image')


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ServiceDetailSerializer(serializers.ModelSerializer):
    category = ServiceCategoryListSerializer(many=False, read_only=True)
    images = ServiceImageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        exclude = ('miniature', 'show_on_home_page', 'public', 'order', 'views', 'pub_date', 'update')


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
