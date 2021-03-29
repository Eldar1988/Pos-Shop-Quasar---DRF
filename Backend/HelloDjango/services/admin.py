from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Image, Service, ServiceRequest, ServiceBenefit


@admin.register(ServiceRequest)
class ServicesRequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'name', 'phone', 'complete', 'date', 'update')
    list_editable = ('complete',)
    search_fields = ('service__title', 'name', 'phone')
    list_filter = ('complete', 'date', 'update')
    list_per_page = 15


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'order', 'pub_date')
    list_editable = ('title', 'order')
    list_filter = ('pub_date', 'update')
    search_fields = ('title',)
    save_as = True
    save_on_top = True
    list_per_page = 10

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height=30px style="object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Миниатюра'


class ImagesInline(admin.TabularInline):
    model = Image
    extra = 0
    fields = ('get_image', 'image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height=30px style="object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Миниатюра'


class ServiceBenefitsInline(admin.TabularInline):
    model = ServiceBenefit
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'category', 'show_on_home_page', 'public', 'order', 'pub_date')
    list_editable = ('category', 'show_on_home_page', 'public', 'order')
    list_filter = ('category', 'show_on_home_page', 'public', 'pub_date', 'update')
    search_fields = ('title', 'category__title')
    inlines = [ServiceBenefitsInline, ImagesInline]
    save_as = True
    save_on_top = True
    list_per_page = 10

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.miniature.url} height=30px style="object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Миниатюра'
