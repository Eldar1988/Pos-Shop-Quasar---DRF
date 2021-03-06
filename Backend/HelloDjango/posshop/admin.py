from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Info, Page, Contacts, Driver, Social, Client, Slider, Banner, Slide, ShopReview, PrivacyPolicy, \
    Benefit, QuestionAndAnswer

admin.site.register(Info)
admin.site.register(Page)
admin.site.register(Contacts)
admin.site.register(Social)
admin.site.register(Slider)
admin.site.register(PrivacyPolicy)


@admin.register(ShopReview)
class ShopReviewAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'rating', 'order',)
    list_editable = ('name', 'rating', 'order',)
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src={obj.avatar.url} height=30px style="object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Фото'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        if obj.logo:
            return mark_safe(f"<img src={obj.logo.url} height=30px>")

    get_image.short_description = 'Логотип'


@admin.register(Slide)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'url', 'btn_text', 'order')
    list_editable = ('title', 'url', 'btn_text', 'order')

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height: 50px; object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Фото'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'url', 'btn_text', 'contain')
    list_editable = ('title', 'url', 'btn_text', 'contain')
    readonly_fields = ('get_image',)

    save_as = True
    save_on_top = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height: 50px; object-fit: cover; border-radius: 5px;">')

    get_image.short_description = 'Баннер'


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order')
    list_editable = ('icon', 'order')

    save_as = True
    save_on_top = True


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

    save_as = True
    save_on_top = True


@admin.register(QuestionAndAnswer)
class QuestionAndAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)

    save_as = True
    save_on_top = True


admin.site.site_title = 'JS Shop v0.0.1'
admin.site.site_header = 'JS Shop v0.0.1 - администрирование'
