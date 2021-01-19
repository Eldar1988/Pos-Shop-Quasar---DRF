from rest_framework import serializers
from .models import Category, Brand, Label, Product, Image, Review


class ChildCategoryListSerializer(serializers.ModelSerializer):
    """Подкатегория"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Category
        exclude = ('description', 'order')


class CategoryListSerializer(serializers.ModelSerializer):
    """Категория (список)"""
    image = serializers.SerializerMethodField('get_image_url')
    child = ChildCategoryListSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Category
        exclude = ('description', 'order')


class BrandListSerializer(serializers.ModelSerializer):
    """Бренд (список)"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Brand
        exclude = ('description', 'order')


class LabelListSerializer(serializers.ModelSerializer):
    """Список меток"""

    class Meta:
        model = Label
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    """Товары (список)"""
    category = CategoryListSerializer(many=False, read_only=True)
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'price', 'old_price', 'image', 'rating', 'slug')


class ImageSerializer(serializers.ModelSerializer):
    """Дополнительные изображения товаров"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Image
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """ОТзывы к товарам"""

    class Meta:
        model = Review
        exclude = ('pub_date', 'public')


class ChildCategoryDetailSerializer(serializers.ModelSerializer):
    """Категория (детали)"""
    image = serializers.SerializerMethodField('get_image_url')
    products = ProductListSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return obj.image.url

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
        return obj.image.url

    class Meta:
        model = Category
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    """Бренд (детали)"""
    image = serializers.SerializerMethodField('get_image_url')
    products = ProductListSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Brand
        fields = '__all__'


class LabelDetailSerializer(serializers.ModelSerializer):
    """Метка (детали)"""
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Label
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    """Товар (детали)"""
    image = serializers.SerializerMethodField('get_image_url')
    category = CategoryListSerializer(many=False)
    brand = BrandListSerializer(many=False)
    labels = LabelListSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Product
        exclude = ('future', 'hit', 'latest', 'public', 'order', 'pub_date', 'update')


