from django.urls import path
from . import views


urlpatterns = [
    path('payments/', views.PaymentMethodsView.as_view({'get': 'list'})),
    path('create_order/', views.CreateOrderView.as_view()),
    path('call_back/', views.CallBackCreateView.as_view()),
]