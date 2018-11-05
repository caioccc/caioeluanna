from django.contrib import admin

# Register your models here.
from app.models import Rsvp

class RsvpAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cerimonia', 'recepcao')

admin.site.register(Rsvp, RsvpAdmin)