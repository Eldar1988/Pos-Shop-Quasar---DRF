from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Info, Page, Contacts, Driver, Social, Client, Slider, Banner, Slide


admin.site.register(Info)
admin.site.register(Page)
admin.site.register(Contacts)
admin.site.register(Driver)
admin.site.register(Social)
admin.site.register(Slider)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'url')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.logo.url} height=30px>")

    get_image.short_description = 'Логотип'


@admin.register(Slide)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'url', 'btn_text', 'order')
    list_editable = ('title', 'url', 'btn_text', 'order')

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height=50px>")

    get_image.short_description = 'Фото'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'url', 'btn_text', 'contain')
    list_editable = ('title', 'url', 'btn_text', 'contain')

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height=50px>")

    get_image.short_description = 'Баннер'
