from django.urls import path
from . import views


urlpatterns = [
    path('payments/', views.PaymentMethodsView.as_view()),
    path('create_order/', views.CreateOrderView.as_view()),
    path('call_back/', views.CallBackCreateView.as_view()),
    path('google_pay_merchant/', views.GooglePayMerchantView.as_view())
]