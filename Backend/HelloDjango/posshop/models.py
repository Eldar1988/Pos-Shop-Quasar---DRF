from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField


class Info(models.Model):
    """Основная информация"""
    site_url = models.URLField('Адрес вашего магазина', null=True, blank=True,
                               help_text='Например: https://shop.kz (без слэша / в конце)')
    name = models.CharField('Название магазина', max_length=50, null=True, blank=True)
    logo = ThumbnailerImageField('Логотип', upload_to='site/', resize_source={'size': (400, 400), 'crop': 'scale'})
    title = models.CharField('Заголовок сайта', max_length=255, help_text='Будет отображаться на главной + title сайта')
    description = models.TextField('Краткое описание компании', max_length=300, help_text='до 300 символов')
    info = RichTextUploadingField('Полное описание компании')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о магазине'
        verbose_name_plural = '1.1 Информация о магазине'


class Page(models.Model):
    """Информационные страницы"""
    title = models.CharField('Заголовок страницы', max_length=255)
    description = models.TextField('Карткое описание', max_length=200,
                                   help_text='Для тега description не более 200 символов')
    body = RichTextUploadingField('Контент')
    slug = models.SlugField('Slug', help_text='Маленькими буквами на латинице, без пробелов и спецсимволов', null=True,
                            blank=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информационная страница'
        verbose_name_plural = '1.4 Информационные страницы'
        ordering = ('order',)


class PrivacyPolicy(models.Model):
    """Политика конфиденциальности"""
    title = models.CharField('Заголовок', max_length=255, default='Политика конфиденциальности')
    body = RichTextUploadingField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'


class Contacts(models.Model):
    """Контактная информация"""
    title = models.CharField('Заголовок для страницы контактов', max_length=255)
    description = models.TextField('Краткое описание')
    phone = models.CharField('Основной телефон', max_length=20)
    whatsapp = models.CharField('Whatsapp', max_length=20, help_text='в формате 7707*******')
    address = models.TextField('Адрес компании')
    body = RichTextUploadingField('Дополнительная информация', blank=True, null=True)
    map_frame = models.TextField('iframe карты', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = '1.2 Контакты'


class Driver(models.Model):
    """Драйвера"""
    title = models.CharField('Название файла', max_length=255)
    description = models.TextField('Описание файла')
    file = models.FileField('Файл', upload_to='files/')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ('order',)


class Social(models.Model):
    """Социальные сети"""
    title = models.CharField('Название сети', max_length=100)
    icon = models.CharField('Иконка сети', max_length=100, help_text='https://materialdesignicons.com/')
    url = models.URLField('URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'


class Client(models.Model):
    """Клиенты компании"""
    title = models.CharField('Название компании', max_length=255, db_index=True)
    logo = ThumbnailerImageField('Логотип', upload_to='clients/', resize_source={'size': (200, 200), 'crop': 'scale'})
    url = models.URLField('Ссылка на сайт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Slider(models.Model):
    """Слайдер"""
    title = models.CharField('Название слайдера', max_length=255)
    arrows = models.BooleanField('Показать стрелки', default=True)
    dots = models.BooleanField('Показать точки', default=True)
    autoplay = models.BooleanField('Автоматическая смена слайдов', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдeр'
        verbose_name_plural = '1.5 Слайдeр'


class Slide(models.Model):
    """Слайд для слайдера"""
    slider = models.ForeignKey(Slider, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Слайдер', related_name='slides')
    title = models.CharField('Заголовок слайда (необязательно)', max_length=255, null=True, blank=True)
    image = ThumbnailerImageField('Картинка', upload_to='slides/',
                                  resize_source={'size': (1200, 1200), 'crop': 'scale'})
    url = models.CharField('Slug (необязательно)', max_length=255, null=True, blank=True)
    btn_text = models.CharField('Текст на кнопке (необязательно)', max_length=100, null=True, blank=True)
    contain = models.BooleanField('Не растягивать слайд', default=False,
                                  help_text='Слайд не будет растягиваться по ширине слайдера')
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        if self.title:
            return self.title
        return f'{self.id}'

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = '1.6 Слайды'
        ordering = ('order',)


class Banner(models.Model):
    """Баннеры"""
    title = models.CharField('Заголовок баннера', max_length=255)
    image = ThumbnailerImageField('Картинка', upload_to='more/',
                                   resize_source={'size': (600, 600), 'crop': 'scale'}, null=True, blank=True)
    url = models.CharField('Slug', max_length=255, null=True, blank=True)
    btn_text = models.CharField('Текст на кнопке', max_length=50, null=True, blank=True)
    contain = models.BooleanField('Не растягивать баннер', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = '1.7 Баннеры'


class ShopReview(models.Model):
    """Отзывы о магазине"""
    name = models.CharField('Имя', max_length=255)
    avatar = ThumbnailerImageField('Аватар', upload_to='testimonials/',
                                   resize_source={'size': (500, 500), 'crop': 'scale'},
                                   help_text='Желательно размером не более 500х500 пикселей, лицо должно быть в центре')
    text = models.TextField('Отзыв')
    rating = models.PositiveSmallIntegerField('Оценка')
    pub_date = models.DateTimeField('Дата создания', auto_now_add=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв о магазине'
        verbose_name_plural = '1.9 Отзывы о магазине'
        ordering = ('-pub_date',)


class Benefit(models.Model):
    """Преимущества магазина"""
    title = models.CharField('Заголовок преимущества', max_length=100)
    icon = models.CharField('Иконка', max_length=100, help_text='Иконки тут https://materialdesignicons.com/')
    text = models.TextField('Описание', max_length=300, help_text='До 300 символов')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = '1.3 Преимущества'
        ordering = ('order',)


class QuestionAndAnswer(models.Model):
    """Вопросы и ответы"""
    question = models.CharField('Вопрос', max_length=255)
    answer = RichTextUploadingField('Ответ')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = '1.8 Вопросы и ответы'
        ordering = ('order',)



