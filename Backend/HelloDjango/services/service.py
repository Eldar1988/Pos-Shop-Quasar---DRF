import telebot
from shop_settings.models import TelegramBot
from .models import Service
from django.conf import settings


try:
    bot_settings = TelegramBot.objects.last()
except:
    bot_settings = ''

if bot_settings:
    try:
        bot = telebot.TeleBot(bot_settings.token)
        chat_id = bot_settings.chat_id
    except:
        bot = ''
        chat_id = ''


def tg_send_service_request(callback):
    """Заявка на обратный звонок"""
    name = callback['name'].value
    phone = callback['phone'].value
    comment = callback['comment'].value
    service_id = callback['service'].value
    service = Service.objects.get(id=service_id)
    text = f'=====   Заявка на услугу ===== \n\n' \
           f'Имя: {name} \n' \
           f'Телефон: {phone} \n' \
           f'Комментарий: {comment} \n' \
           f'Услуга: {service.title} \n'

    try:
        bot.send_message(chat_id, text)
    except:
        return