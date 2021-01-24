from rest_framework import serializers
from django.conf import settings
from .models import Page, Info, Contacts, Driver, Social, Client, Slider, Banner, Slide, ShopReview, PrivacyPolicy, \
    Benefit, QuestionAndAnswer


class ShopReviewSerializer(serializers.ModelSerializer):
    """Отзывы о магазине"""
    avatar = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.avatar.url}'

    class Meta:
        model = ShopReview
        exclude = ('order', 'pub_date')


class PagesListSerializer(serializers.ModelSerializer):
    """Информационные страницы (спсиок)"""

    class Meta:
        model = Page
        exclude = ('body', 'order', 'description')


class ShortInfoSerializer(serializers.ModelSerializer):
    """Краткая информация о компании"""
    logo = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.logo.url}'

    class Meta:
        model = Info
        exclude = ('info',)


class InfoSerializer(serializers.ModelSerializer):
    """Полная информация о компании"""
    logo = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.logo.url}'

    class Meta:
        model = Info
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    """Контактная информация"""

    class Meta:
        model = Contacts
        fields = '__all__'


class DriversSerializer(serializers.ModelSerializer):
    """Драйвера"""
    file = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return f'{settings.APP_PATH}{obj.file.url}'

    class Meta:
        model = Driver
        fields = '__all__'


class SocialsSerializer(serializers.ModelSerializer):
    """Социальные сети"""

    class Meta:
        model = Social
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    """Клиенты магазина"""
    logo = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.logo.url}'

    class Meta:
        model = Client
        fields = '__all__'


class SlidesSerializer(serializers.ModelSerializer):
    """Слайды"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Slide
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    """Слайдер"""
    slides = SlidesSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.img.url}'

    class Meta:
        model = Slider
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    """Баннер"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return f'{settings.APP_PATH}{obj.image.url}'

    class Meta:
        model = Banner
        fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):
    """Политика конфиденицальности"""

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class PageDetailSerializer(serializers.ModelSerializer):
    """Информационные страницы"""

    class Meta:
        model = Page
        fields = '__all__'


class BenefitSerializer(serializers.ModelSerializer):
    """Преимущества"""

    class Meta:
        model = Benefit
        exclude = ('order',)


class QuestionAndAnswerSerializer(serializers.ModelSerializer):
    """Вопросы и ответы"""
    class Meta:
        model = QuestionAndAnswer
        exclude = ('order',)



