from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import generics
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response

import random

from .models import Product, Category, Label, Brand
from .serializers import ProductListSerializer, CategoryDetailSerializer, ProductDetailSerializer, \
    LabelDetailSerializer, BrandDetailSerializer, ReviewSerializer, CategoryListSerializer
from .service import ProductsPagination


class CategoriesListView(generics.ListAPIView):
    """All categories"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class HomeHitProductsView(generics.ListAPIView):
    """Hit products for home page"""
    queryset = Product.objects.filter(public=True, hit=True, show_on_home_page=True)[:30]
    serializer_class = ProductListSerializer


class HomeSaleProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(public=True, old_price__gte=1, show_on_home_page=True)[:30]
    serializer_class = ProductListSerializer


class LatestProductsView(generics.ListAPIView):
    """Latest products. Limit 20"""
    queryset = Product.objects.filter(public=True, latest=True, show_on_home_page=True)[:20]
    serializer_class = ProductListSerializer


class HomeFutureProducts(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(public=True, future=True, show_on_home_page=True)[:30]
    serializer_class = ProductListSerializer


class CategoryDetailView(APIView):
    """Категория детали"""

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        category_serializer = CategoryDetailSerializer(category, many=False)
        return Response(category_serializer.data)


class ProductListView(generics.ListAPIView):
    """Список товаров"""
    queryset = Product.objects.filter(public=True)
    serializer_class = ProductListSerializer
    pagination_class = ProductsPagination


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

        categories = ['Мужские кофты', 'Платья']
        count = 1
        images = [
            'https://cvetogis.kz/wp-content/uploads/2021/03/belo-roz-300x400.jpg',
            'https://cvetogis.kz/wp-content/uploads/2021/03/kremovye-300x400.jpg',
            'https://cvetogis.kz/wp-content/uploads/2021/03/belaya-300x400.jpg',
            'https://cvetogis.kz/wp-content/uploads/2021/03/krasnaya-300x400.jpg',
            'https://cvetogis.kz/wp-content/uploads/2021/02/3-.jpg',
            'https://cvetogis.kz/wp-content/uploads/2021/02/3-bel.jpg',
            'https://cvetogis.kz/wp-content/uploads/2021/02/3-.jpg'
        ]
        brands = ['fashion_5', 'Fashion 4', 'Fashion 3', 'Fashion 2']

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
                price=random.uniform(3000, 1000000),
                miniature_url=random.choice(images),
                image_url=random.choice(images),
                rating=random.uniform(2, 5),
                in_stock_quantity=20
            )
            count += 1

        return Response(status=201)
