from django.contrib import admin

from formulaire.models import Data


class DataAdmin(admin.ModelAdmin):
    list_display=('name', 'file')
    
admin.site.register(Data, DataAdmin)
