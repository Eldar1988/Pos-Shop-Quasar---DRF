from django.contrib import admin
from .models import MainColor, Script, TelegramBot


admin.site.register(Script)
admin.site.register(TelegramBot)


@admin.register(MainColor)
class MainColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'primary_color', 'accent_color', 'body_color', 'positive_color', 'footer_color', 'alert_color')
    list_editable = ('primary_color', 'accent_color', 'body_color', 'positive_color', 'footer_color', 'alert_color')

