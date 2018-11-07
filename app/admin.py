from django.contrib import admin

# Register your models here.
from app.models import Rsvp, Recado, Produto


class RsvpAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cerimonia', 'recepcao')


class RecadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'aprovado')


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'parcelas', 'categoria', 'url')


admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(Recado, RecadoAdmin)
admin.site.register(Produto, ProdutoAdmin)
