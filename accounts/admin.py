from django.contrib import admin

from .models import ClientAccountToken


# Register your models here.
@admin.register(ClientAccountToken)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'refresh_token', 'access_token', 'date')
    list_per_page = 10
    list_display_links = 'id',
