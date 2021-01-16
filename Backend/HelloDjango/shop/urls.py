from django.urls import path
from . import views

urlpatterns = [
    # Товары со скидкой
    path('home_sale_products/', views.HomeSaleProductView.as_view({'get': 'list'})),
    # Рекомендуемые товары
    path('home_future_products/', views.HomeFutureProducts.as_view({'get': 'list'})),
]