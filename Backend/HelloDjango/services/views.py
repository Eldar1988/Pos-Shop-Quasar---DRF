from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Service, ServiceRequest, Category
from .serializers import ServiceCategoryListSerializer, ServiceCategoryDetailSerializer, \
    ServiceDetailSerializer, ServiceRequestSerializer


class CategoriesListView(generics.ListAPIView):
    """Список категорий услуг"""
    queryset = Category.objects.all()
    serializer_class = ServiceCategoryListSerializer


class AllServicesView(generics.ListAPIView):
    """Список всех категорий и услуг"""
    queryset = Category.objects.all()
    serializer_class = ServiceCategoryDetailSerializer


class CategoryDetailView(APIView):
    """Детали категории по slug"""
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        serializer = ServiceCategoryDetailSerializer(category, many=False)
        return Response(serializer.data)


class ServiceDetailView(APIView):
    """Детали услуги по id"""
    def get(self, request, pk):
        service = Service.objects.get(id=pk)
        serializer = ServiceDetailSerializer(service, many=False)
        return Response(serializer.data)


class CreateServiceRequestView(APIView):
    """Создание заявки на услугу"""
    def post(self, request):
        serializer = ServiceRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
