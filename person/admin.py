from django.contrib import admin
from django.http import FileResponse

from reports.planilha import Planilha

from .models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "data_nascimento", "idade", "ativo", "valor")
    list_filter = (
        "ativo",
        "valor",
    )
    search_fields = ("nome", "email")
    readonly_fields = ("idade",)
    actions = ["exportar_relatorio"]

    def idade(self, obj):
        return obj.idade

    def exportar_relatorio(self, request, queryset):
        """
        Gera e exporta um relatório das pessoas
        """
        planilha, titulo = Planilha.get_planilha(queryset=queryset)
        response = FileResponse(planilha, as_attachment=True, filename=f"{titulo}.xlsx")
        return response

    exportar_relatorio.short_description = (
        "Exportar relatório Excel das pessoas selecionadas"
    )


admin.site.register(Pessoa, PessoaAdmin)
