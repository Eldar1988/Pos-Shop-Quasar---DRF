from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('shop/', include('shop.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
    path('', include('posshop.urls')),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += doc_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
