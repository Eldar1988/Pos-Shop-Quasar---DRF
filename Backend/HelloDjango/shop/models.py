from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
from easy_thumbnails.fields import ThumbnailerImageField


class Category(models.Model):
    main_category = models.BooleanField('Главная', default=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Родительская категория', related_name='child')
    title = models.CharField('Название категории', max_length=255)
    slug = models.SlugField('Slug', unique=True, help_text='Маленькие буквы на латинице без пробелов и спецсимволов')
    label = models.CharField('Ярлык', max_length=50, help_text='Например: "Скидки до 50%"', null=True, blank=True)
    description = models.TextField('Описание категории', max_length=300, help_text='Не более 300 символов',
                                   null=True, blank=True)
    full_description = RichTextUploadingField('Полное описание', null=True, blank=True)
    image = ThumbnailerImageField('Изображение', upload_to='categories/',
                                  resize_source={'size': (170, 170), 'crop': 'scale'},
                                  help_text='Пропорции 1:1 (квадрат)')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = '2.1 Категории'
        ordering = ('order',)


class Brand(models.Model):
    title = models.CharField('Название бренда', max_length=255)
    slug = models.SlugField('Slug', unique=True, help_text='Маленькие буквы на латинице без пробелов и спецсимволов')
    description = models.TextField('Описание бренда', max_length=200, help_text='Не болле 200 символов',
                                   null=True, blank=True)
    full_description = RichTextUploadingField('Полное описание', null=True, blank=True)
    image = ThumbnailerImageField('Логотип', upload_to='brands/',
                                  resize_source={'size': (200, 200), 'crop': 'scale'},
                                  help_text='Пропорции 1:1 (квадрат)')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = '2.2 Бренды'
        ordering = ('order',)


class Label(models.Model):
    title = models.CharField('Метка товара', max_length=255)
    slug = models.SlugField('Slug', unique=True, help_text='Маленькие буквы на латинице без пробелов и спецсимволов')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Метка товара'
        verbose_name_plural = '2.3 Метки товаров'
        ordering = ('order',)


class CharacteristicType(models.Model):
    """Типы характеристики"""
    title = models.CharField('Название', max_length=255)
    category = models.ManyToManyField(Category, blank=True, verbose_name='Категории',
                                      related_name='characteristic_types',
                                      help_text='Укажите категории, в которых будут использоватьс характеристики')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип характеристики'
        verbose_name_plural = '2.7 Типы характеристик'
        ordering = ('order',)


class Characteristic(models.Model):
    """Харатктеристика товара"""
    type = models.ForeignKey(CharacteristicType, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Выберите тип', related_name='characteristics')
    value = models.CharField('Значение', max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = '2.8 Характеристики'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Категория', related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Бренд', related_name='products')
    labels = models.ManyToManyField(Label, blank=True, verbose_name='Метки', related_name='products')
    characteristics = models.ManyToManyField(Characteristic, verbose_name='Характеристки', blank=True,
                                             related_name='products')
    title = models.CharField('Название товара', max_length=255, db_index=True)
    article = models.CharField('Артикул товара', max_length=100, blank=True, null=True)
    description = models.TextField('Краткое описание товара', max_length=300, help_text='Не более 300 символов')
    info = RichTextUploadingField('Дополнительная информация', null=True, blank=True, help_text='Необязательно')
    characteristic = RichTextUploadingField('Характеристики', null=True, blank=True, help_text='Необязательно')
    video = models.CharField('Видео с Youtube', max_length=255, null=True, blank=True,
                             help_text='Скопировать код в url после знака =')
    price = models.IntegerField('Цена товара', null=True, blank=True)
    old_price = models.IntegerField('Старая цена', null=True, blank=True, help_text='Необязательно')
    purchase_price = models.IntegerField('Закуп', null=True, blank=True,
                                         help_text='Закупочная стоимость товара (необязательно)', default=0)
    price_comment = models.CharField('Комментарий к цене', null=True, blank=True, max_length=255,
                                     help_text='Например: цена по запросу. Будет показан только в случае, если не указана цена товара')
    image = ThumbnailerImageField('Миниатюра', upload_to='products/', null=True, blank=True,
                                  resize_source={'size': (300, 300), 'crop': 'scale'},
                                  help_text='Пропорции 1:1 (квадрат). Будет использоваться в каталоге товаров')
    miniature_url = models.URLField('URL миниатюры', null=True, blank=True,
                                    help_text='Добавлять в том случае, если ваши изображения хранятся в другом месте, и их можно получить по ссылке')
    full_image = ThumbnailerImageField('Фото товара', upload_to='products/', null=True, blank=True,
                                       resize_source={'size': (1200, 1200), 'crop': 'scale'},
                                       help_text='Пропорции 1:1 (квадрат). Будет использоваться на странице товара')
    image_url = models.URLField('URL фото', null=True, blank=True,
                                help_text='Добавлять в том случае, если ваши изображения хранятся в другом месте, и их можно получить по ссылке')
    image_contain = models.BooleanField('Растянуть фото товара', default=False,
                                        help_text='Фото растянется на всю высоту и ширину карточки, '
                                                  'с сохранением пропорций')
    rating = models.PositiveSmallIntegerField('Рейтинг товара', default=5, null=True, blank=True)
    show_on_home_page = models.BooleanField('На главной', default=False,
                                            help_text='Отобразить товар на главной странице')
    future = models.BooleanField('Рекомендуем?', default=False)
    hit = models.BooleanField('Хит продаж', default=False)
    latest = models.BooleanField('Новинка', default=False)
    public = models.BooleanField('Опубликовать', default=True)
    in_stock_quantity = models.IntegerField('В наличии', default=0)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    shipping_detail = models.TextField('Условия доставки',
                                       default='Доставка по всему Казахстану<br>'
                                               'Стоимость доставки расчитывается отдельно от заказа<br>'
                                               'При заказе на сумму свыше 50 000 тг доставка бесплатная',
                                       max_length=255,
                                       help_text='Используйте br для переноса строки, если нужен перенос строки')
    views = models.IntegerField('Кол-во просмотров', default=0)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'{settings.SITE_URL}/#/product/{self.id}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = '2.4 Товары'
        ordering = ('order', 'price')


class VariationType(models.Model):
    """Типы вариаций для товаров"""
    title = models.CharField('Заголовок', max_length=255)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True,
                                             help_text='Необходимо для сортировки (необязательно)')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
        verbose_name = 'Тип вариации'
        verbose_name_plural = '2.6 Типы вариаций'


class Variation(models.Model):
    """Вариации товаров"""
    type = models.ForeignKey(VariationType, on_delete=models.SET_NULL, verbose_name='Тип вариации',
                             related_name='variations', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Товар', related_name='variations')
    value = models.CharField('Значение', max_length=255)
    price = models.IntegerField('Цена', null=True, blank=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ('order',)
        verbose_name = 'Вариация'
        verbose_name_plural = 'Вариации'


class Image(models.Model):
    image = ThumbnailerImageField('Фото товара', upload_to='products/',
                                  resize_source={'size': (1200, 1200), 'crop': 'scale'})
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Товар',
                                related_name='images')
    contain = models.BooleanField('Растянуть фото товара', default=False,
                                  help_text='Фото растянется на всю высоту и ширину карточки, с сохранением пропорций')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'


class Video(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Товар', related_name='videos')
    video = models.CharField('Видео с Youtube', max_length=255, help_text='Скопировать код в url после знака =')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Дополнительное видео'
        verbose_name_plural = 'Дополнительное видео'
        ordering = ('order',)


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
        verbose_name_plural = '2.5 Отзывы'
        ordering = ('-pub_date',)
