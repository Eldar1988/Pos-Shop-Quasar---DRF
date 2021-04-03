from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    # Метка детали
    path('label/<slug:slug>/', views.LabelDetailView.as_view()),
    # Бренд детали
    path('brand/<slug:slug>/', views.BrandDetailView.as_view()),
    # Товары со скидкой
    path('home_sale_products/', views.HomeSaleProductView.as_view({'get': 'list'})),
    # Рекомендуемые товары
    path('home_future_products/', views.HomeFutureProducts.as_view({'get': 'list'})),
    # Хиты продаж
    path('home_hit_products/', views.HomeHitProductsView.as_view()),
    # Новинки
    path('latest_products/', views.LatestProductsView.as_view()),
    # Категория детали
    path('category/<slug:slug>/', views.CategoryDetailView.as_view()),

    # Товар детали
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
    # + Отзыв
    path('create_review/', views.CreateReviewView.as_view()),
    # Поиск товаров
    path('search/', views.SearchView.as_view()),
    path('set_stock/<int:value>/', views.SetInStockQuantity.as_view()),
    path('categories/', views.CategoriesListView.as_view()),
    path('create_random_product/<int:quantity>/', views.CreateProducts.as_view())
]
