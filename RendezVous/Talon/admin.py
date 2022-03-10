from django.contrib import admin

from .models import Talon


@admin.register(Talon)
class SerialNumberAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    search_fields = ['user.phone_number', ]
    list_display = ('user', 'order', 'creation_date', )
    ordering = ('-order', )
