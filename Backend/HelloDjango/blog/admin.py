from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'slug']
    list_editable = ['order', 'slug']

    save_as = True
    save_on_top = True


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'title', 'category', 'order', 'slug', 'public', 'date']
    list_editable = ['category', 'order', 'slug', 'public']
    list_display_links = ['get_image', 'title']
    list_filter = ['category', 'public', 'date', 'update']
    # inlines = [CommentInline]
    filter_horizontal = ('services', 'products')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height=50px style="object-fit: cover">')


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post', 'public', 'date', 'update']
#     list_editable = ['public']
#     list_filter = ['public', 'date', 'update']
#     search_fields = ['name', 'comment']

