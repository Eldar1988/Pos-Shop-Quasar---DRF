from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Order, OrderItem, PaymentMethod, CallBack


admin.site.register(PaymentMethod)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    readonly_fields = ('price', 'quantity', 'item_sum', 'variations')
    fields = ('product', 'price', 'quantity', 'item_sum', 'variations')
    show_change_link = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'payment_method', 'order_sum', 'city', 'region', 'paid', 'completed', 'created', 'updated']
    list_filter = ['paid', 'payment_method', 'paid', 'completed', 'created', 'updated']
    list_editable = ['paid', 'completed']
    inlines = [OrderItemInline]
    list_display_links = ['id', 'name']
    search_fields = ['name', 'phone', 'notice', 'id', 'city', 'region']
    list_per_page = 20


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'processed', 'date', 'update']
    list_filter = ['processed', 'date', 'update']
    list_editable = ['processed']
    readonly_fields = ['name', 'phone', 'date', 'update']
    search_fields = ['name', 'phone', 'notice']

