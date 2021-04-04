from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters

from .models import Product


class ProductsPagination(PageNumberPagination):
    page_size = 30
    max_page_size = 100


class ChaFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductsFilter(filters.FilterSet):
    price = filters.RangeFilter()
    category = ChaFilterInFilter(field_name='category_id')
    brand = ChaFilterInFilter(field_name='brand__slug')
    category_slug = ChaFilterInFilter(field_name='category__slug')
    title = ChaFilterInFilter(field_name='title', lookup_expr='in')
    label = ChaFilterInFilter(field_name='labels__slug')
    characteristics = ChaFilterInFilter(field_name='characteristics__value')

    class Meta:
        model = Product
        fields = ['category', 'title', 'price', 'category_slug', 'brand', 'label', 'characteristics']


