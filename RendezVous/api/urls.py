from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings

from .client import urls as client_urls
from .open_api import schema_view

urlpatterns = [
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),
    path('client/', include(client_urls), name='client'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
