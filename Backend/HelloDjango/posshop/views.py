from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Info, Page, Contacts, Social, Client, Slider, Banner
from .serializers import ShortInfoSerializer, PagesListSerializer, ContactInfoSerializer, SocialsSerializer, \
    ClientsSerializer, SliderSerializer, BannerSerializer

from shop.models import Category, Brand, Product
from shop.serializers import CategoryListSerializer, BrandListSerializer, ProductListSerializer


class MainInfoView(APIView):
    """Основная информация для сайта"""

    def get(self, request):
        response_data = {}

        info = Info.objects.last()
        info_serializer = ShortInfoSerializer(info, many=False)
        response_data['companyInfo'] = info_serializer.data

        pages = Page.objects.all()
        pages_serializer = PagesListSerializer(pages, many=True)
        response_data['pages'] = pages_serializer.data

        contacts = Contacts.objects.last()
        contacts_serializer = ContactInfoSerializer(contacts, many=False)
        response_data['contacts'] = contacts_serializer.data

        socials = Social.objects.all()
        socials_serializer = SocialsSerializer(socials, many=True)
        response_data['socials'] = socials_serializer.data

        clients = Client.objects.all()
        clients_serializer = ClientsSerializer(clients, many=True)
        response_data['clients'] = clients_serializer.data

        slider = Slider.objects.all()
        slider_serializer = SliderSerializer(slider, many=True)
        response_data['slider'] = slider_serializer.data

        banners = Banner.objects.all()
        banners_serializer = BannerSerializer(banners, many=True)
        response_data['banners'] = banners_serializer.data

        categories = Category.objects.all()
        categories_serializer = CategoryListSerializer(categories, many=True)
        response_data['categories'] = categories_serializer.data

        brands = Brand.objects.all()
        brands_serializer = BrandListSerializer(brands, many=True)
        response_data['brands'] = brands_serializer.data

        hit_products = Product.objects.filter(public=True, hit=True, show_on_home_page=True)
        products_serializer = ProductListSerializer(hit_products, many=True)
        response_data['hitProducts'] = products_serializer.data

        return Response(response_data)

