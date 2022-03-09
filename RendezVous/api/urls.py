from django.urls import path, include

from .client import urls as client_urls
from .open_api import schema_view


urlpatterns = [
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),
    path('client/', include(client_urls), name='client'),
]
