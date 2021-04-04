from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
from django.utils.safestring import mark_safe
from .models import Category, Brand, Label, Product, Image, Review, Video, VariationType, Variation, CharacteristicType, Characteristic


admin.site.register(VariationType)


@admin.register(CharacteristicType)
class CharacteristicTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_products_count', 'order')
    list_editable = ('order',)
    list_filter = (('category', admin.RelatedOnlyFieldListFilter),)
    search_fields = ('title',)
    filter_horizontal = ('category',)

    def get_products_count(self, obj):
        characteristics = Characteristic.objects.filter(type=obj).count()
        return characteristics

    get_products_count.short_description = 'Значения'


@admin.register(Characteristic)
class CharacteristicsAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_filter = ('type',)
    search_fields = ('type__title', 'value')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'main_category', 'parent', 'order', 'get_products_count')
    list_editable = ('order', 'parent')
    list_display_links = ('get_image', 'title')
    search_fields = ('title',)
    list_filter = (('parent', admin.RelatedOnlyFieldListFilter), 'main_category')
    readonly_fields = ('get_image',)
    prepopulated_fields = {"slug": ("title",)}
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Миниатюра'

    def get_products_count(self, obj):
        products = Product.objects.filter(category=obj).count()
        return products

    get_products_count.short_description = 'Товары'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'order', 'get_products_count')
    list_editable = ('order',)
    search_fields = ('title',)
    readonly_fields = ('get_image',)
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 20
    list_display_links = ('get_image', 'title')

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Лого'

    def get_products_count(self, obj):
        products = Product.objects.filter(brand=obj).count()
        return products

    get_products_count.short_description = 'Товары'


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'get_products_count')
    list_editable = ('order',)
    search_fields = ('title',)
    list_per_page = 20
    prepopulated_fields = {"slug": ("title",)}

    save_as = True
    save_on_top = True

    def get_products_count(self, obj):
        products = Product.objects.filter(labels=obj).count()
        return products

    get_products_count.short_description = 'Товары'


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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating', 'pub_date', 'public')
    list_editable = ('rating', 'public')
    readonly_fields = ('name', 'text')
    search_fields = ('name', 'text')
    list_filter = ('public', 'pub_date', 'rating')
    list_per_page = 10

    save_as = True
    save_on_top = True


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0


@admin.register(Product)
class ProductAdmin(TabbedModelAdmin):
    model = Product
    ordering = ('-pub_date',)
    date_hierarchy = 'pub_date'

    readonly_fields = ('get_image', 'get_full_image', 'pub_date', 'update')
    filter_horizontal = ('labels', 'characteristics')
    list_display = ('get_image', 'title', 'category', 'price', 'old_price', 'purchase_price',
                    'in_stock_quantity', 'show_on_home_page', 'future', 'hit', 'latest', 'public', 'order')
    list_editable = ('category', 'price', 'old_price', 'purchase_price', 'in_stock_quantity',
                     'future', 'hit', 'latest', 'public', 'order', 'show_on_home_page')
    list_filter = (('category', admin.RelatedOnlyFieldListFilter), 'brand', 'future', 'hit', 'latest', 'public', 'order', 'labels', 'pub_date',
                   'update', 'rating', ('characteristics', admin.RelatedOnlyFieldListFilter))
    search_fields = ('title', 'category__title', 'brand__title', 'article', 'characteristics__value',
                     'characteristics__type__title')
    list_display_links = ('get_image', 'title')

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
            'fields': ('price', 'old_price', 'purchase_price', 'price_comment', 'in_stock_quantity')
        }),
    )
    tab_media = (
        (None, {
            'fields': ('image', 'miniature_url', 'full_image', 'image_url', 'image_contain', 'video', 'get_image', 'get_full_image')
        }),
        VideoInline,
        ImageInline
    )
    tab_shipping = (
        (None, {
            'fields': ('shipping_detail',)
        }),
    )
    tab_characteristics = (
        (None, {
            'fields': ('characteristics',)
        }),
    )
    tab_more_details = (
        (None, {
            'fields': ('show_on_home_page', 'future', 'hit', 'latest', 'public', 'rating', 'order', 'pub_date',
                       'update', 'views')
        }),
        ReviewInline
    )
    tab_variations = (
        VariationInline,
    )

    tabs = [
        ('Главное', tab_main_info),
        ('Описание', tab_description),
        ('Цена', tab_price),
        ('Медиа', tab_media),
        ('Доставка', tab_shipping),
        ('Дополнительно', tab_more_details),
        ('Харакетристики', tab_characteristics),
        ('Вариации', tab_variations)
    ]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px;">')
        elif obj.miniature_url:
            return mark_safe(
                f'<img src={obj.miniature_url} style="height: 50px; width: 50px; object-fit: cover; border-radius: 5px;">')

    def get_full_image(self, obj):
        if obj.full_image:
            return mark_safe(
                f'<img src={obj.full_image.url} style="height: 150px; width: 150px; object-fit: cover; border-radius: 5px;">')
        elif obj.image_url:
            return mark_safe(
                f'<img src={obj.image_url} style="height: 150px; width: 150px; object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Миниатюра'
    get_full_image.short_description = 'Полное изображение'
