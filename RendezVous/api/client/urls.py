from django.urls import path

from .views import *

urlpatterns = [
    path('create_client/', ClientView.as_view(), name='client'),
    path('activate/<uidb64>/<token>',
         ActivateAccountView.as_view(), name='activate'),
]
