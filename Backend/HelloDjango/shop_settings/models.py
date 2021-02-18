from django.db import models
from colorfield.fields import ColorField


class MainColor(models.Model):
    """Настройки цвета"""
    primary_color = ColorField('Основной цвет', default='#523ee8')
    accent_color = ColorField('Дополнительный цвет', help_text='Кнопки и переключатели', default='#f73859')
    body_color = ColorField('Цвет текста', default='#31475e')
    positive_color = ColorField('Цвет сообщений об успехе', default='#21BA45')
    alert_color = ColorField('Цвет предупреждений', default='#f73859')
    footer_color = ColorField('Цвет футера сайта', default='#523ee8')

    def __str__(self):
        return f'{self.id}. Настройки цвета'

    class Meta:
        verbose_name = 'Основной цвет'
        verbose_name_plural = '4.1 Основные цвета'


class Script(models.Model):
    """Скрипты дополнительные"""
    title = models.CharField('Заголовок', max_length=100, help_text='Например: Яндекс метрика')
    script = models.TextField('Скрипт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скрипт'
        verbose_name_plural = '4.3 Скрипты'


class ProductCardSettings(models.Model):
    """Настройка карточки товаров"""
    height = models.PositiveIntegerField('Высота картинки товара в карточке (px)', default=200,
                                         help_text='Ширина примет значение автоматически с сохранением пропорций')

    def __str__(self):
        return f'Настройки карточки товара #{self.id}'

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = '4.2 Карточка товаров'


class TelegramBot(models.Model):
    """Настройки бота телеграм"""
    name = models.CharField('Имя бота', max_length=100)
    token = models.CharField('Token', max_length=155)
    chat_id = models.CharField('Chat_id', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Telegram bot'
        verbose_name_plural = '4.4 Telegram bot'


