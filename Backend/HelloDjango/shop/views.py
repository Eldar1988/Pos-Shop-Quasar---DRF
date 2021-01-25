from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product, Category, Label, Brand
from .serializers import ProductListSerializer, CategoryDetailSerializer, ProductDetailSerializer, \
    LabelDetailSerializer, BrandDetailSerializer, ReviewSerializer
from .service import ProductsPagination


class HomeSaleProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(public=True, old_price__gte=1, show_on_home_page=True)[:30]
    serializer_class = ProductListSerializer
    pagination_class = ProductsPagination


class HomeFutureProducts(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(public=True, future=True, show_on_home_page=True)[:30]
    serializer_class = ProductListSerializer
    pagination_class = ProductsPagination


class CategoryDetailView(APIView):
    """Категория детали"""

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        category_serializer = CategoryDetailSerializer(category, many=False)
        return Response(category_serializer.data)


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

    def get(self, request, slug):
        response_data = {}
        product = Product.objects.get(slug=slug)
        product_serializer = ProductDetailSerializer(product, many=False)
        response_data['product'] = product_serializer.data
        products = Product.objects.filter(
            category_id=product.category_id, public=True).exclude(id=product.id).order_by('?')[:20]
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


