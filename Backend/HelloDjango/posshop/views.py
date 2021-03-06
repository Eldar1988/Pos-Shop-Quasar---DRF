from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Info, Page, Contacts, Social, Client, Slider, Banner, ShopReview, PrivacyPolicy, Benefit, \
    QuestionAndAnswer, Driver
from .serializers import ShortInfoSerializer, PagesListSerializer, ContactInfoSerializer, SocialsSerializer, \
    ClientsSerializer, SliderSerializer, BannerSerializer, ShopReviewSerializer, PrivacyPolicySerializer, \
    PageDetailSerializer, InfoSerializer, BenefitSerializer, QuestionAndAnswerSerializer, DriversSerializer

from shop.models import Category, Brand, Product
from shop.serializers import CategoryListSerializer, BrandListSerializer, ProductListSerializer

from shop_settings.service import get_settings


class MainInfoView(APIView):
    """Основная информация для сайта"""

    def get(self, request):
        response_data = {'settings': get_settings()}

        # categories = Category.objects.all()
        # categories_serializer = CategoryListSerializer(categories, many=True)
        # response_data['categories'] = categories_serializer.data

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

        slider = Slider.objects.last()
        slider_serializer = SliderSerializer(slider, many=False)
        response_data['slider'] = slider_serializer.data

        brands = Brand.objects.all()
        brands_serializer = BrandListSerializer(brands, many=True)
        response_data['brands'] = brands_serializer.data

        # hit_products = Product.objects.filter(public=True, hit=True, show_on_home_page=True)[:30]
        # products_serializer = ProductListSerializer(hit_products, many=True)
        # response_data['hitProducts'] = products_serializer.data

        # latest_products = Product.objects.filter(public=True, latest=True, show_on_home_page=True)[:20]
        # products_serializer = ProductListSerializer(latest_products, many=True)
        # response_data['latestProducts'] = products_serializer.data

        reviews = ShopReview.objects.all()
        reviews_serializer = ShopReviewSerializer(reviews, many=True)
        response_data['reviews'] = reviews_serializer.data

        benefits = Benefit.objects.all()
        benefits_serializer = BenefitSerializer(benefits, many=True)
        response_data['benefits'] = benefits_serializer.data

        return Response(response_data)


class PrivacyPolicyView(APIView):
    """Политика конфиденциальности"""

    def get(self, request):
        policy = PrivacyPolicy.objects.last()
        serializer = PrivacyPolicySerializer(policy, many=False)
        return Response(serializer.data)


class InfoPageDetailView(APIView):
    """Информационная страница"""

    def get(self, request, slug):
        page = Page.objects.get(slug=slug)
        serializer = PageDetailSerializer(page, many=False)
        return Response(serializer.data)


class AboutShopDetailView(APIView):
    """О магазине"""

    def get(self, request):
        about = Info.objects.last()
        serializer = InfoSerializer(about, many=False)
        return Response(serializer.data)


class BannersView(APIView):
    """Баннеры (3 баннера рандомным выбором)"""

    def get(self, request):
        banners = Banner.objects.all().order_by('?')[:3]
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)


class QuestionsView(APIView):
    """Вопросы и ответы"""

    def get(self, request):
        questions = QuestionAndAnswer.objects.all()
        serializer = QuestionAndAnswerSerializer(questions, many=True)
        return Response(serializer.data)


class DriversView(APIView):
    """Файлы"""

    def get(self, request):
        files = Driver.objects.all()
        serializer = DriversSerializer(files, many=True)
        return Response(serializer.data)
