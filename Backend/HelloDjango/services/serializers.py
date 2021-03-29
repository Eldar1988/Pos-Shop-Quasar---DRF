from rest_framework import serializers
from django.conf import settings

from .models import Category, Service, Image, ServiceRequest, ServiceBenefit


class ServiceCategoryListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'slug')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'


class ServiceListSerializer(serializers.ModelSerializer):
    miniature = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'miniature')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.miniature.url}'


class ServiceCategoryDetailSerializer(serializers.ModelSerializer):
    services = ServiceListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        exclude = ('pub_date', 'update', 'order', 'image')


class ServiceImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Image
        fields = '__all__'

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'


class ServiceBenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBenefit
        fields = '__all__'


class ServiceDetailSerializer(serializers.ModelSerializer):
    category = ServiceCategoryListSerializer(many=False, read_only=True)
    images = ServiceImageSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField('get_image_url')
    benefits = ServiceBenefitsSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        exclude = ('miniature', 'show_on_home_page', 'public', 'order', 'views', 'pub_date', 'update')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'

