from django.contrib import admin

# Register your models here.
from app.models import Rsvp, Recado


class RsvpAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cerimonia', 'recepcao')


class RecadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'aprovado')


admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(Recado, RecadoAdmin)
