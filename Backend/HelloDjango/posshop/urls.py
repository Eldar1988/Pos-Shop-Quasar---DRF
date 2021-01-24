from django.urls import path
from . import views

urlpatterns = [
    path('banners/', views.BannersView.as_view({'get': 'list'})),
    path('privacy_policy/', views.PrivacyPolicyView.as_view()),
    path('info_page/<slug:slug>/', views.InfoPageDetailView.as_view()),
    path('about/', views.AboutShopDetailView.as_view()),
    path('questions/', views.QuestionsView.as_view()),
    path('', views.MainInfoView.as_view()),
]
