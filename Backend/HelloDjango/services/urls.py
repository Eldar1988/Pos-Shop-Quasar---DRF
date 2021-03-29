from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoriesListView.as_view()),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view()),
    path('service/<int:pk>/', views.ServiceDetailView.as_view()),
    path('create_service_request/', views.CreateServiceRequestView.as_view())
]