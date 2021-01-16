from django.urls import path
from . import views

urlpatterns = [
    path('banners/', views.BannersView.as_view({'get': 'list'})),
    path('', views.MainInfoView.as_view()),
]
