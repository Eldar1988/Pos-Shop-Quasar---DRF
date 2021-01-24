from django.urls import path
from . import views

urlpatterns = [
    # Метка детали
    path('label/<slug:slug>/', views.LabelDetailView.as_view()),
    # Бренд детали
    path('brand/<slug:slug>/', views.BrandDetailView.as_view()),
    # Товары со скидкой
    path('home_sale_products/', views.HomeSaleProductView.as_view({'get': 'list'})),
    # Рекомендуемые товары
    path('home_future_products/', views.HomeFutureProducts.as_view({'get': 'list'})),
    # Категория детали
    path('category/<slug:slug>/', views.CategoryDetailView.as_view()),
    # Товар детали
    path('product/<slug:slug>/', views.ProductDetailView.as_view()),
    # + Отзыв
    path('create_review/', views.CreateReviewView.as_view()),
    # Поиск товаров
    path('search/', views.SearchView.as_view()),
]