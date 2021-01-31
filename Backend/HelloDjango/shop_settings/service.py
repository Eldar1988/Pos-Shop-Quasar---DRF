from .models import MainColor, Script
from .serializers import MainColorSerializer, ScriptSerializer, ProductCardSettingsSerializer, ProductCardSettings


def get_settings():
    settings = {}

    colors = MainColor.objects.last()
    colors_serializer = MainColorSerializer(colors, many=False)

    scripts = Script.objects.all()
    scripts_serializer = ScriptSerializer(scripts, many=True)

    product_card_settings = ProductCardSettings.objects.last()
    product_card_settings_serializer = ProductCardSettingsSerializer(product_card_settings, many=False)

    settings['colors'] = colors_serializer.data
    settings['scripts'] = scripts_serializer.data
    settings['productCardSettings'] = product_card_settings_serializer.data

    return settings
