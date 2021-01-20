from django.http import HttpResponse
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import PaymentMethod, Order, OrderItem
from .serializers import PaymentMethodSerializer

from .tg_bot import tg_send_order


class PaymentMethodsView(viewsets.ReadOnlyModelViewSet):
    """Способы оплаты"""
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


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

        return HttpResponse('success')
