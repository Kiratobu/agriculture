from django.contrib import admin

# Register your models here.

from agriculture.models import (
    Farmer,
    Culture,
    Plot,
    Season
)



@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
 
@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    

admin.site.register(Plot)
admin.site.register(Season)