from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField
from cloudinary.models import CloudinaryField
from shop.models import Product


class PaymentMethod(models.Model):
    """Способо оплаты"""
    title = models.CharField('Заголовок способа оплаты', max_length=255)
    image = ThumbnailerImageField('Картинка', upload_to='payments/', resize_source={'size': (200, 200), 'crop': 'scale'})
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = '3.3 Способы оплаты'
        ordering = ('order',)


class Order(models.Model):
    """Заказ"""
    name = models.CharField('ФИО покупателя', max_length=100, db_index=True)
    phone = models.CharField('Телефон покупателя', max_length=20)
    email = models.EmailField('Email покупателя', null=True, blank=True)
    region = models.CharField('Область', max_length=200)
    city = models.CharField('Город', max_length=200)
    address = models.CharField('Адрес', max_length=200)
    order_sum = models.DecimalField('Общая сумма заказа', max_digits=15, decimal_places=0, null=True, blank=True)
    payment_method = models.CharField('Способ оплаты', max_length=200, null=True, blank=True)
    notice = models.TextField('Заметка', null=True, blank=True)
    created = models.DateTimeField('Заказано', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)
    paid = models.BooleanField('Оплачено', default=False)
    completed = models.BooleanField('Выполнено', default=False)

    def __str__(self):
        return f'{self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = '3.1 Заказы'
        ordering = ('-created',)


class OrderItem(models.Model):
    """Товар заказа"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_items',
                                verbose_name='Товар')
    variations = models.TextField('Вариации', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0)
    quantity = models.PositiveSmallIntegerField('Количество', default=1)
    item_sum = models.IntegerField('Итого', null=True, blank=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


class CallBack(models.Model):
    """Обратный звонок"""
    name = models.TextField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=30)
    notice = models.TextField('Заметка', null=True, blank=True)
    processed = models.BooleanField('Обработано', default=False)
    date = models.DateTimeField('Дата', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = '3.2 Заявки (обратный звонок)'
        ordering = ('-date',)

