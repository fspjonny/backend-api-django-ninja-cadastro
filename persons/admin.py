from django.contrib import admin

from .models import PersonsModel


# Register your models here.
@admin.register(PersonsModel)
class PersonsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'sexo', 'nascimento', 'rg', 'cpf', 'email', 'telefone',
        'pai', 'mae', 'endereco', 'cargo', 'salario', 'admissao')
    list_per_page = 10
    list_display_links = 'nome',
    list_filter = 'nome', 'rg', 'cpf', 'email'

