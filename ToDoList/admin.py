from django.contrib import admin

# Register your models here.
from .models import Informations


class InformationsAdmin(admin.ModelAdmin):
    list_display = ('text', 'flag',)

admin.site.register(Informations,InformationsAdmin)