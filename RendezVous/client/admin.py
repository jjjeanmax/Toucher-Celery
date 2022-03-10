from django.contrib import admin

from .models import ClientProfile


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'email_confirmed', 'last_name', 'first_name', 'created_at',)

    readonly_fields = ('id',)

    def has_add_permission(self, request):
        return True
