from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductListSerializer
from .service import ProductsPagination


class HomeSaleProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(public=True, old_price__gte=1, show_on_home_page=True)[:30]
    serializer_class = ProductListSerializer
    pagination_class = ProductsPagination


class HomeFutureProducts(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(public=True, future=True, show_on_home_page=True)[:30]
    serializer_class = ProductListSerializer
    pagination_class = ProductsPagination
