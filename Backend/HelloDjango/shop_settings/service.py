from .models import MainColor, Script
from .serializers import MainColorSerializer, ScriptSerializer


def get_settings():
    settings = {}

    colors = MainColor.objects.last()
    colors_serializer = MainColorSerializer(colors, many=False)

    scripts = Script.objects.all()
    scripts_serializer = ScriptSerializer(scripts, many=True)

    settings['colors'] = colors_serializer.data
    settings['scripts'] = scripts_serializer.data

    return settings
