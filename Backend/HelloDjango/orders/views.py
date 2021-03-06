import random
import string
import hashlib
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .tg_bot import tg_send_order, tg_send_call_back

from .models import PaymentMethod, Order, OrderItem, GooglePay
from .serializers import PaymentMethodSerializer, CallBackCreateSerializer, GooglePaySerializer
from shop.serializers import ProductDetailSerializer
from shop.models import Product


class PaymentMethodsView(APIView):
    """Способы оплаты"""

    def get(self, request):
        payments = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(payments, many=True)
        return Response(serializer.data)


class GooglePayMerchantView(APIView):
    """Google pay data"""

    def get(self, request):
        merchant = GooglePay.objects.last()
        serializer = GooglePaySerializer(merchant, many=False)
        return Response(serializer.data)


class CallBackCreateView(APIView):
    def post(self, request):
        serializer = CallBackCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            tg_send_call_back(serializer)
            return Response(status=201)

        print(serializer.errors)


class CreateOrderView(APIView):
    def post(self, request):
        data = request.data
        order = Order.objects.create(
            name=str(data['name']),
            phone=str(data['phone']),
            email=str(data['email']),
            region=str(data['region']),
            city=str(data['city']),
            address=str(data['address']),
            order_sum=(data['order_sum']),
            payment_method=(data['payment_method']),
            paid=(data['paid']),
            notice=(data['notice'])
        )
        for i in data['products']:
            if i['price'] is None:
                i['price'] = 0
            OrderItem.objects.create(
                order=order,
                product_id=i['id'],
                price=i['price'],
                quantity=i['quantity'],
                variations=i['variations'],
                item_sum=i['price']*i['quantity']
            )

        tg_send_order(order)

        for i in data['products']:
            product = Product.objects.get(id=i['id'])
            product.in_stock_quantity -= i['quantity']
            product.save()

        return Response(status=201)


