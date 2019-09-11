from django.contrib import admin

from core.models import Tarefa


class TarefaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'feito']


admin.site.register(Tarefa, TarefaAdmin)
