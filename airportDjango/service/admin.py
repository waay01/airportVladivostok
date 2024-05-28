from django.contrib import admin
from service.models import *


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('placeName',)
    ordering = ('placeName',)


@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_place', 'timeWork')
    ordering = ('title',)


@admin.register(Foods)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_place', 'timeWork')
    ordering = ('title',)
