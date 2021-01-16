from django.urls import path
from . import views

urlpatterns = [
    # Товары со скидкой
    path('sale_products/', views.SaleProductView.as_view({'get': 'list'})),
    # Рекомендуемые товары
    path('future_products/', views.FutureProducts.as_view({'get': 'list'})),
]