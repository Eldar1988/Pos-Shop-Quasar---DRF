from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Родительская категория', related_name='child')
    title = models.CharField('Название категории', max_length=255)
    description = models.TextField('Описание категории', max_length=200, help_text='Не болле 200 символов')
    full_description = RichTextUploadingField('Полное описание', null=True, blank=True)
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
    full_description = RichTextUploadingField('Полное описание', null=True, blank=True)
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
    labels = models.ManyToManyField(Label, blank=True, verbose_name='Метки', related_name='products')
    title = models.CharField('Название товара', max_length=255, db_index=True)
    article = models.CharField('Артикул товара', max_length=100, blank=True, null=True)
    description = models.TextField('Краткое описание товара', max_length=300, help_text='Не более 300 символов')
    info = RichTextUploadingField('Дополнительная информация', null=True, blank=True, help_text='Необязательно')
    characteristic = RichTextUploadingField('Характеристики', null=True, blank=True, help_text='Необязательно')
    video = models.CharField('Видео обзор с Youtube', max_length=255, null=True, blank=True,
                             help_text='Скопировать код в url после знака =')
    price = models.PositiveSmallIntegerField('Цена товара')
    old_price = models.PositiveSmallIntegerField('Старая цена', null=True, blank=True, help_text='Необязательно')
    image = CloudinaryField('Основное изображение товара', folder='posShop/products')
    rating = models.PositiveSmallIntegerField('Рейтинг товара', default=5)
    show_on_home_page = models.BooleanField('На главной', default=False, help_text='Отобразить товар на глваной странице')
    future = models.BooleanField('Рекомендуем?', default=False)
    hit = models.BooleanField('Хит продаж', default=False)
    latest = models.BooleanField('Новинка', default=False)
    public = models.BooleanField('Опубликовать', default=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('order', 'price')


class Image(models.Model):
    image = CloudinaryField('Избражение', folder='posShop/products')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Товар', related_name='images')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Товар', related_name='reviews')
    name = models.CharField('Имя', max_length=255)
    text = models.TextField('Отзыв')
    rating = models.PositiveSmallIntegerField('Оценка')
    pub_date = models.DateTimeField('Дата создания', auto_now_add=True)
    public = models.BooleanField('Опубликовать', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)
