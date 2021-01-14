from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Brand, Label, Product, Image, Option, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'slug', 'order')
    list_editable = ('title', 'slug', 'order')
    search_fields = ('title',)

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height=30px>")

    get_image.short_description = 'Миниатюра'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'slug', 'order')
    list_editable = ('title', 'slug', 'order')
    search_fields = ('title',)

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height=30px>")

    get_image.short_description = 'Лого'


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('slug', 'order')
    search_fields = ('title',)

    save_as = True
    save_on_top = True


class ImageInline(admin.TabularInline):
    model = Image


class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'category', 'brand', 'price', 'old_price', 'rating', 'future', 'hit', 'latest', 'public', 'order')
    list_editable = ('title', 'category', 'brand', 'price', 'old_price', 'rating', 'future', 'hit', 'latest', 'public', 'order')
    list_filter = ('category', 'brand', 'rating', 'future', 'hit', 'latest', 'public', 'order', 'labels', 'pub_date', 'update')
    search_fields = ('title',)
    filter_horizontal = ('labels',)
    filter_vertical = ('labels',)
    inlines = [ImageInline, ReviewInline]
    fields = [
        ('title', 'article'),
        ('category', 'brand'),
        ('price', 'old_price'),
        ('image',), ('description',),
        ('future', 'hit', 'latest', 'public'),
        ('kaspi_url', 'kaspi_kod'),
        ('labels',),
        ('info',),
        ('rating', 'order'),
        ('pub_date', 'update')
    ]
    readonly_fields = ('pub_date', 'update')

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height=30px>")

    get_image.short_description = 'Фото'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'product')
    list_editable = ('title',)
    search_fields = ('title',)

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height=30px>")

    get_image.short_description = 'Миниатюра'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating', 'pub_date', 'public')
    list_editable = ('rating', 'public', 'product')
    readonly_fields = ('name', 'text')
    search_fields = ('name', 'text')

    save_as = True
    save_on_top = True
