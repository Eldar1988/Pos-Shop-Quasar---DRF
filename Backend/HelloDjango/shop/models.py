from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField


class Category(models.Model):
    title = models.CharField('Название категории', max_length=255)
    description = models.TextField('Описание категории', max_length=200, help_text='Не болле 200 символов')
    image = CloudinaryField('Миниатюра', folder='posShop/categories')
    slug = models.SlugField('Slug', unique=True, help_text='Маленькие буквы на латинице без пробелов и спецсимволов')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order',)


class Brand(models.Model):
    title = models.CharField('Название бренда', max_length=255)
    description = models.TextField('Описание бренда', max_length=200, help_text='Не болле 200 символов')
    image = CloudinaryField('Логотип', folder='posShop/brands')
    slug = models.SlugField('Slug', unique=True, help_text='Маленькие буквы на латинице без пробелов и спецсимволов')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ('order',)


class Label(models.Model):
    title = models.CharField('Метка товара', max_length=255)
    slug = models.SlugField('Slug', unique=True, help_text='Маленькие буквы на латинице без пробелов и спецсимволов')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Метка товара'
        verbose_name_plural = 'Метки товара'
        ordering = ('order',)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Категория', related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Бренд', related_name='products')
    title = models.CharField('Название товара', max_length=255)
    article = models.CharField('Артикул товара', blank=True, null=True)
    image = CloudinaryField('Основное изображение товара', folder='posShop/products')
    price = models.PositiveSmallIntegerField('Цена товара')
    old_price = models.PositiveSmallIntegerField('Старая цена товара (необзяательно)', null=True, blank=True)
    description = models.TextField('Краткое описание товара')
    info = RichTextUploadingField('Дополнительная информация', null=True, blank=True)
    rating = models.PositiveSmallIntegerField('Рейтинг товара', default=5)
    kaspi_url = models.URLField('Ссылка на kaspi', blank=True, null=True)
    kaspi_kod = models.TextField('Код html kaspi', blank=True, null=True)
    future = models.BooleanField('Рекомендуем?', default=False)
    hit = models.BooleanField('Хит продаж', default=False)
    latest = models.BooleanField('Новинка', default=False)
    public = models.BooleanField('Опубликовать', default=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('order',)


class Image(models.Model):
    title = models.CharField('Название фото', max_length=255)
    image = CloudinaryField('Избражение', folder='posShop/products')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Товар', related_name='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'

class Option(models.Model):
    title = models.CharField('')