from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Order, OrderItem, PaymentMethod


admin.site.register(PaymentMethod)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    readonly_fields = ('price', 'quantity', 'item_sum')
    fields = ('product', 'price', 'quantity', 'item_sum')
    show_change_link = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'payment_method', 'order_sum', 'city', 'paid', 'completed', 'created', 'updated']
    list_filter = ['paid', 'payment_method', 'paid', 'completed', 'created', 'updated']
    list_editable = ['paid', 'completed']
    inlines = [OrderItemInline]
    list_display_links = ['id', 'name']
    search_fields = ['name', 'phone', 'notice', 'id', 'city', 'region']
