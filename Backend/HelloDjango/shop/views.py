from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductListSerializer
from .service import ProductsPagination


class SaleProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(public=True, old_price__gte=1)
    serializer_class = ProductListSerializer
    pagination_class = ProductsPagination


class FutureProducts(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(public=True, future=True)
    serializer_class = ProductListSerializer
    pagination_class = ProductsPagination
