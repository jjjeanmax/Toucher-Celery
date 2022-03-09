from django.contrib import admin

from .models import ClientProfile


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

    def has_add_permission(self, request):
        return True
