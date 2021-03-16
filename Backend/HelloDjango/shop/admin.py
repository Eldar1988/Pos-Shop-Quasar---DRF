from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
from django.utils.safestring import mark_safe
from .models import Category, Brand, Label, Product, Image, Review, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'parent', 'slug', 'order')
    list_editable = ('title', 'slug', 'order', 'parent')
    search_fields = ('title',)
    list_filter = ('parent',)
    readonly_fields = ('get_image',)

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Миниатюра'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'slug', 'order')
    list_editable = ('title', 'slug', 'order')
    search_fields = ('title',)
    readonly_fields = ('get_image',)
    list_per_page = 10

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Лого'


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('slug', 'order')
    search_fields = ('title',)
    list_per_page = 10

    save_as = True
    save_on_top = True


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Миниатюра'


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     # prepopulated_fields = {'slug': ('title',)}
#     list_display = ('get_image', 'title', 'category', 'brand', 'price', 'old_price', 'purchase_price', 'in_stock_quantity', 'rating', 'show_on_home_page',
#                     'future', 'hit', 'latest', 'public', 'order')
#     list_editable = ('title', 'category', 'price', 'old_price', 'purchase_price', 'in_stock_quantity', 'rating', 'future', 'hit', 'latest', 'public', 'order', 'show_on_home_page')
#     list_filter = ('category', 'brand', 'rating', 'future', 'hit', 'latest', 'public', 'order', 'labels', 'pub_date', 'update')
#     search_fields = ('title',)
#     filter_horizontal = ('labels',)
#     list_per_page = 10
#     inlines = [, ReviewInline]
#     fields = [
#         (),
#         (),
#         (),
#         ()
#     ]
#     readonly_fields = ('get_image', 'get_full_image', 'pub_date', 'update', 'views')
#
#     save_as = True
#     save_on_top = True
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: contain;">')
#
#     def get_full_image(self, obj):
#         return mark_safe(f'<img src={obj.full_image.url} style="height: 50px; width: 50px; object-fit: contain;">')
#
#     get_image.short_description = 'Миниатюра'
#     get_full_image.short_description = 'Фото'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating', 'pub_date', 'public')
    list_editable = ('rating', 'public', 'product')
    readonly_fields = ('name', 'text')
    search_fields = ('name', 'text')
    list_filter = ('public', 'pub_date', 'rating')
    list_per_page = 10

    save_as = True
    save_on_top = True


@admin.register(Product)
class ProductAdmin(TabbedModelAdmin):
    model = Product
    readonly_fields = ('get_image', 'get_full_image', 'pub_date', 'update')
    filter_horizontal = ('labels',)
    list_display = ('get_image', 'title', 'category', 'brand', 'price', 'old_price', 'purchase_price',
                    'in_stock_quantity', 'rating', 'show_on_home_page', 'future', 'hit', 'latest', 'public', 'order')
    list_editable = ('title', 'category', 'price', 'old_price', 'purchase_price', 'in_stock_quantity', 'rating',
                     'future', 'hit', 'latest', 'public', 'order', 'show_on_home_page')
    list_filter = ('category', 'brand', 'future', 'hit', 'latest', 'public', 'order', 'labels', 'pub_date',
                   'update', 'rating')
    search_fields = ('title', 'category__title', 'brand__title')

    list_per_page = 10
    save_as = True
    save_on_top = True

    tab_main_info = (
        (None, {
            'fields':
                ('category', 'brand', 'title', 'article', 'labels')
        }),

    )
    tab_description = (
        (None, {
            'fields': ('description', 'characteristic', 'info')
        }),
    )
    tab_price = (
        (None, {
            'fields': ('price', 'old_price', 'purchase_price', 'in_stock_quantity')
        }),
    )
    tab_media = (
        (None, {
            'fields': ('image', 'full_image', 'image_contain', 'video', 'get_image', 'get_full_image')
        }),
        VideoInline,
        ImageInline
    )
    tab_shipping = (
        (None, {
            'fields': ('shipping_detail',)
        }),
    )
    tab_more_details = (
        (None, {
            'fields': ('show_on_home_page', 'future', 'hit', 'latest', 'public', 'rating', 'order', 'pub_date',
                       'update', 'views')
        }),
        ReviewInline
    )

    tabs = [
        ('Главное', tab_main_info),
        ('Описание', tab_description),
        ('Цена', tab_price),
        ('Медиа', tab_media),
        ('Доставка', tab_shipping),
        ('Дополнительно', tab_more_details),
    ]

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px;">')

    def get_full_image(self, obj):
        return mark_safe(
            f'<img src={obj.full_image.url} style="height: 150px; width: 150px; object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Миниатюра'
    get_full_image.short_description = 'Полное изображение'
