from rest_framework import serializers
from .models import Category, Brand, Label, Product, Image, Review, Video
from django.conf import settings


class ChildCategoryListSerializer(serializers.ModelSerializer):
    """Подкатегория"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Category
        exclude = ('description', 'order', 'full_description')


class CategoryListSerializer(serializers.ModelSerializer):
    """Категория (список)"""
    image = serializers.SerializerMethodField('get_image_url')
    child = ChildCategoryListSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Category
        exclude = ('description', 'order', 'full_description')


class BrandListSerializer(serializers.ModelSerializer):
    """Бренд (список)"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Brand
        exclude = ('description', 'order', 'full_description')


class LabelListSerializer(serializers.ModelSerializer):
    """Список меток"""

    class Meta:
        model = Label
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    """Товары (список)"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'price', 'old_price', 'image', 'rating', 'image_contain')


class ImageSerializer(serializers.ModelSerializer):
    """Дополнительные изображения товаров"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Image
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """ОТзывы к товарам"""

    class Meta:
        model = Review
        exclude = ('pub_date',)


class ChildCategoryDetailSerializer(serializers.ModelSerializer):
    """Категория (детали)"""
    image = serializers.SerializerMethodField('get_image_url')
    products = ProductListSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Категория (детали)"""
    image = serializers.SerializerMethodField('get_image_url')
    products = ProductListSerializer(many=True, read_only=True)
    child = ChildCategoryDetailSerializer(many=True, read_only=True)
    parent = ChildCategoryListSerializer(many=False, read_only=True)

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Category
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    """Бренд (детали)"""
    image = serializers.SerializerMethodField('get_image_url')
    products = ProductListSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Brand
        fields = '__all__'


class LabelDetailSerializer(serializers.ModelSerializer):
    """Метка (детали)"""
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Label
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    """Дополнительное виедо товара"""
    class Meta:
        model = Video
        exclude = ('order', 'product')


class ProductDetailSerializer(serializers.ModelSerializer):
    """Товар (детали)"""
    full_image = serializers.SerializerMethodField('get_full_image_url')
    image = serializers.SerializerMethodField('get_image_url')
    category = CategoryListSerializer(many=False)
    brand = BrandListSerializer(many=False)
    labels = LabelListSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    def get_full_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.full_image.url}'

    class Meta:
        model = Product
        exclude = ('future', 'hit', 'latest', 'public', 'order', 'pub_date', 'update', 'purchase_price')


