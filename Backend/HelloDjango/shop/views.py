from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import generics
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response
import django_filters.rest_framework

import random

from .models import Product, Category, Label, Brand
from .serializers import ProductListSerializer, CategoryDetailSerializer, ProductDetailSerializer, \
    LabelDetailSerializer, BrandDetailSerializer, ReviewSerializer, CategoryListSerializer
from .service import ProductsPagination, ProductsFilter


class CategoriesListView(APIView):
    """Список всех категорий"""

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class HomeHitProductsView(APIView):
    """Хиты продаж для главной страницы (до 30 единиц)"""

    def get(self, request):
        products = Product.objects.filter(public=True, hit=True, show_on_home_page=True)[:30]
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class HomeSaleProductView(APIView):
    """Товары со скидкой для главной страницы (до 30 единиц)"""

    def get(self, request):
        products = Product.objects.filter(public=True, old_price__gte=1, show_on_home_page=True)[:30]
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class LatestProductsView(APIView):
    """Новинки для главной страницы (до 20 единиц)"""

    def get(self, request):
        products = Product.objects.filter(public=True, latest=True, show_on_home_page=True)[:20]
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class HomeFutureProducts(APIView):
    """Рекомендуемый товар для главной страницы (до 20 единиц)"""

    def get(self, request):
        products = Product.objects.filter(public=True, future=True, show_on_home_page=True)[:30]
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class CategoryDetailView(APIView):
    """Категория детали"""

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        category_serializer = CategoryDetailSerializer(category, many=False)
        return Response(category_serializer.data)


class ProductListView(generics.ListAPIView):
    """Список товаров"""
    serializer_class = ProductListSerializer
    pagination_class = ProductsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductsFilter

    def get_queryset(self):
        queryset = Product.objects.filter(public=True)
        if self.request.query_params.get('order_by') == 'priceFromMax':
            queryset = Product.objects.filter(public=True).order_by('-price')

        if self.request.query_params.get('order_by') == 'date':
            queryset = Product.objects.filter(public=True).order_by('-pub_date')

        if self.request.query_params.get('order_by') == 'rating':
            queryset = Product.objects.filter(public=True).order_by('-rating')

        return queryset


class LabelDetailView(APIView):
    """Категория детали"""

    def get(self, request, slug):
        label = Label.objects.get(slug=slug)
        label_serializer = LabelDetailSerializer(label, many=False)
        return Response(label_serializer.data)


class BrandDetailView(APIView):
    """Бренд детали"""

    def get(self, request, slug):
        brand = Brand.objects.get(slug=slug)
        brand_serializer = BrandDetailSerializer(brand, many=False)
        return Response(brand_serializer.data)


class ProductDetailView(APIView):
    """Детали товара"""

    def get(self, request, pk):
        response_data = {}
        product = Product.objects.get(id=pk)
        product_serializer = ProductDetailSerializer(product, many=False)
        response_data['product'] = product_serializer.data
        products = Product.objects.filter(
            category_id=product.category_id, public=True).exclude(id=product.id).order_by('?')[:10]
        products_serializer = ProductListSerializer(products, many=True)
        response_data['products'] = products_serializer.data

        product.views += 1
        product.save()

        return Response(response_data)


class CreateReviewView(APIView):
    """Создание отзывы"""

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

        print(serializer.errors)

        return Response(status=500)


class SearchView(APIView):
    """Результаты поиска"""
    def get(self, request):
        search_request = request.GET.get('search')
        products = Product.objects.filter(title__icontains=search_request)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class SetInStockQuantity(View):
    """Установка количества в наличии для всех товаров"""
    def get(self, request, value):
        products = Product.objects.all()
        if request.user.is_authenticated and request.user.is_staff:
            for i in products:
                i.in_stock_quantity = value
                i.save()

            return HttpResponse(f'Операция выполнена, изменено {products.count()} товаров.')

        return HttpResponse('У Вас недосаточно прав...')


class CreateProducts(APIView):
    def get(self, request, quantity):

        categories = ['Майки', 'Футболки']
        count = 1
        images = [
            'https://ae01.alicdn.com/kf/H9b5e8f7e12fd4feab3af3964d78ad7bbb/-.jpg_q50.jpg',
            'https://ae01.alicdn.com/kf/H9b5e8f7e12fd4feab3af3964d78ad7bbb/-.jpg_q50.jpg',
            'https://i5.walmartimages.com/asr/1aee6f35-1b05-4afd-9db1-61c4aeb0214c_1.5a39c700945f8e7a5e4c70c37ef0a983.jpeg',
            'https://g.excellentorigin.co/img/products/56031-erkek-tops-goemlek-alfabe-serisi-fil-ve-kz-bask-yeni-t-shirt-oezel-oezel-ksa-kollu-tee-shirt-siyah-tisoert.jpg'
        ]
        brands = ['nike', 'adidas']
        show_on_home_page = [True, False, False, False]
        future = [True, False, False, False]
        hit = [True, False, False, False]
        latest = [True, False, False, False]

        for i in range(quantity):
            category = Category.objects.get(title=random.choice(categories))
            brand = Brand.objects.get(title=random.choice(brands))

            Product.objects.create(
                category=category,
                brand=brand,
                title=f'Test product {count}',
                description='Краткое описание товара',
                info='Дополнительная информация',
                characteristic='Характеристики',
                price=random.uniform(3000, 500000),
                miniature_url=random.choice(images),
                image_url=random.choice(images),
                rating=random.uniform(2, 5),
                in_stock_quantity=20
            )
            count += 1

        return Response(status=201)
