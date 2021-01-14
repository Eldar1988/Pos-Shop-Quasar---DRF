from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor_uploader.fields import RichTextUploadingField


class Info(models.Model):
    """Основная информация"""
    logo = CloudinaryField('Логотип', folder='posshop')
    title = models.CharField('Заголовок сайта', max_length=255, help_text='Будет отображаться на главной + title сайта')
    description = models.TextField('Краткое описание компании', max_length=200, help_text='до 200 символов')
    info = RichTextUploadingField('Полное описание компании')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о магазине'
        verbose_name_plural = 'Информация о магазине'


class Page(models.Model):
    """Информационные страницы"""
    title = models.CharField('Заголовок страницы', max_length=255)
    description = models.TextField('Карткое описание', max_length=200, help_text='Для тега description не более 200 символов')
    body = RichTextUploadingField('Контент')
    slug = models.SlugField('Slug', help_text='Маленькими буквами на латинице, без пробелов и спецсимволов', null=True, blank=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информационная страница'
        verbose_name_plural = 'Информационные страницы'
        ordering = ('order',)


class Contacts(models.Model):
    """Контактная иформация"""
    title = models.CharField('Заголовок для страницы контактов', max_length=255)
    description = models.TextField('Краткое описание')
    phone = models.CharField('Основной телефон', max_length=20)
    whatsapp = models.CharField('Whatsapp', max_length=20, help_text='в формате 7707*******')
    address = models.TextField('Адрес компании')
    body = RichTextUploadingField('Дополнительная информация')
    map_frame = models.TextField('iframe карты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Driver(models.Model):
    """Драйвера"""
    title = models.CharField('Название драйвера', max_length=255)
    description = models.TextField('Описание драйвера')
    file = models.FileField('Файл', upload_to='drivers/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Драйвер'
        verbose_name_plural = 'Драйвера'


class Social(models.Model):
    title = models.CharField('Название сети', max_length=100)
    icon = models.CharField('Иконка сети', max_length=100, help_text='https://materialdesignicons.com/')
    url = models.URLField('URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural ='Социальные сети'


class Client(models.Model):
    """Клиенты компании"""
    title = models.CharField('Название компании', max_length=255, db_index=True)
    logo = CloudinaryField('Логотип', folder='posshop/clients')
    url = models.URLField('Ссылка на сайт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Slider(models.Model):
    title = models.CharField('Заголовок слайда', max_length=255)
    image = CloudinaryField('Картинка', folder='poshop/sldies')
    url = models.SlugField('Slug')
    btn_text = models.CharField('Текст на кнопке', max_length=100)
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер'
        ordering = ('order',)


class Banner(models.Model):
    title = models.CharField('Заголовок Баннера', max_length=255)
    image = CloudinaryField('Картинка', folder='poshop/sldies')
    url = models.SlugField('Slug')
    btn_text = models.CharField('Текст на кнопке', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
