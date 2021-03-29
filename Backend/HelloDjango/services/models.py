from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Category(models.Model):
    """Категория услуг"""
    title = models.CharField('Заголовок категории', max_length=255)
    description = models.TextField('Краткое описание', max_length=200, help_text='Необходимо для CEO')
    image = ThumbnailerImageField('Миниатюра категории', upload_to='services_category/',
                                  resize_source={'size': (170, 170), 'crop': 'scale'})
    slug = models.SlugField('Slug', unique=True, help_text='Маленькие буквы на латинице без пробелов и спецсимволов')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True,
                                             help_text='Необходим для сортировки')
    pub_date = models.DateTimeField('Опубликовано', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = '5.1 Категории услуг'
        ordering = ('-pub_date', 'order')


class Service(models.Model):
    """Услуга"""
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Категория', related_name='services')
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Краткое описание', max_length=300, help_text='Необходимо для CEO')
    miniature = ThumbnailerImageField('Миниатюра услуги', upload_to='services_miniatures/',
                                      resize_source={'size': (300, 300), 'crop': 'scale'})
    image = ThumbnailerImageField('Фото услуги', upload_to='services/',
                                  resize_source={'size': (1200, 1200), 'crop': 'scale'})
    body = RichTextUploadingField('Полное описание услуги')
    call_to_action = models.TextField('Текст-призыв к действию', null=True, blank=True)
    btn_text = models.CharField('Текст-призыв на кнопке', default='Консультация', max_length=100)
    video = models.CharField('Видео с Youtube (необязательно)', max_length=255, null=True, blank=True,
                             help_text='Скопировать код в url после знака =')
    show_on_home_page = models.BooleanField('На главной', default=False,
                                            help_text='Отобразить товар на главной странице')
    public = models.BooleanField('Опубликовать', default=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True,
                                             help_text='Необходим для сортировки')
    views = models.IntegerField('Кол-во просмотров', default=0)
    pub_date = models.DateTimeField('Опубликовано', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = '5.2 Услуги'
        ordering = ('-pub_date', 'order')


class ServiceRequest(models.Model):
    """Заявка на услугу"""
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Услуга',
                                related_name='requests')
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=20)
    comment = models.TextField('Комментарий', null=True, blank=True)
    complete = models.BooleanField('Обработано', default=False)
    body = RichTextUploadingField('Заметки (для личного пользования)', null=True, blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на услугу'
        verbose_name_plural = '5.3 Заявки на услуги'
        ordering = ('-date',)


class ServiceBenefit(models.Model):
    """Преимущество услуги"""
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Преимущество услуги', related_name='benefits')
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Описание')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True,
                                             help_text='Необходим для сортировки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Перимущество'
        verbose_name_plural = 'Преимущества услуги'
        ordering = ('order',)


class Image(models.Model):
    image = ThumbnailerImageField('Фото товара', upload_to='services/',
                                  resize_source={'size': (1200, 1200), 'crop': 'scale'})
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Услуга',
                                related_name='images')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'
