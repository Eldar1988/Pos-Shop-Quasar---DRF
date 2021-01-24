from django.contrib import admin
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
        return mark_safe(f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: contain;">')

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
        return mark_safe(f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: contain;">')

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
        return mark_safe(f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: cover;">')

    get_image.short_description = 'Миниатюра'


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'category', 'brand', 'price', 'old_price', 'rating', 'show_on_home_page',
                    'future', 'hit', 'latest', 'public', 'order')
    list_editable = ('title', 'price', 'category', 'old_price', 'rating', 'future', 'hit', 'latest', 'public', 'order', 'show_on_home_page')
    list_filter = ('category', 'brand', 'rating', 'future', 'hit', 'latest', 'public', 'order', 'labels', 'pub_date', 'update')
    search_fields = ('title',)
    filter_horizontal = ('labels',)
    filter_vertical = ('labels',)
    list_per_page = 10
    inlines = [VideoInline, ImageInline, ReviewInline]
    fields = [
        ('title', 'article', 'slug'),
        ('category', 'brand'),
        ('price', 'old_price'),
        ('image', 'get_image'),
        ('full_image', 'get_full_image'),
        ('image_contain'),
        ('description',),
        ('show_on_home_page','future', 'hit', 'latest', 'public'),
        ('labels',),
        ('info',),
        ('characteristic',),
        ('video', 'rating', 'order'),
        ('pub_date', 'update')
    ]
    readonly_fields = ('get_image', 'get_full_image', 'pub_date', 'update')

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: contain;">')

    def get_full_image(self, obj):
        return mark_safe(f'<img src={obj.full_image.url} style="height: 50px; width: 50px; object-fit: contain;">')

    get_image.short_description = 'Миниатюра'
    get_full_image.short_description = 'Фото'


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
