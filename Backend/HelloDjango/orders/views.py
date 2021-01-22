from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .tg_bot import tg_send_order, tg_send_call_back

from .models import PaymentMethod, Order, OrderItem
from .serializers import PaymentMethodSerializer, CallBackCreateSerializer
from shop.serializers import ProductDetailSerializer


class PaymentMethodsView(viewsets.ReadOnlyModelViewSet):
    """Способы оплаты"""
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


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
            payment_method=(data['payment_method'])
        )
        for i in data['products']:
            OrderItem.objects.create(
                order=order,
                product_id=i['id'],
                price=i['price'],
                quantity=i['quantity'],
                item_sum=i['price']*i['quantity']
            )

        tg_send_order(order)
        serializer = ProductDetailSerializer(many=False)

        return Response(serializer.data)
