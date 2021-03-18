import telebot
from .models import OrderItem
from shop_settings.models import TelegramBot

from django.conf import settings

try:
    bot_settings = TelegramBot.objects.last()
except:
    bot_settings = ''
# bot = telebot.TeleBot('1587261399:AAF_VbkxIue05PA6JnkNYAHvXyH9oISwuU8')
# chat_id = '-1001374586109'
#
if bot_settings:
    try:
        bot = telebot.TeleBot(bot_settings.token)
        chat_id = bot_settings.chat_id
    except:
        bot = ''
        chat_id = ''


def tg_send_call_back(callback):
    """Заявка на обратный звонок"""
    name = callback['name'].value
    phone = callback['phone'].value
    text = f'=====   Обратный звонок ===== \n\n' \
           f'Имя: {name} \n' \
           f'Телефон: {phone} \n'

    try:
        bot.send_message(chat_id, text)
    except:
        return


def tg_send_order(order):
    """Новый заказ"""
    order_items = OrderItem.objects.filter(order_id=order.id)
    text = f"=== Новый заказ # 100{order} === \n\n" \
           "Заказчик: \n" \
           f"Имя: {order.name}\n" \
           f"Телефон: {order.phone} \n" \
           f"Email: {order.email} \n" \
           "====================== \n" \
           f"Область: {order.region} \n" \
           f"Город: {order.city} \n" \
           f"Адрес: {order.address} \n" \
           "====================== \n" \
           f"Общая сумма заказа: {order.order_sum} тг \n" \
           f"Способ оплаты: {order.payment_method} \n\n" \
           "===== Товары в заказе ===== \n"

    for i in order_items:
        text_order = f"{i.product} \n" \
                     f"Цена: {i.price} тг \n" \
                     f"Количество: {i.quantity} \n" \
                     f"Итого: {i.item_sum} тг \n" \
                     f"Фото: {settings.APP_PATH + i.product.image.url} \n" \
                     "================= \n"

        text += text_order

    try:
        bot.send_message(chat_id, text=text)
    except:
        return
