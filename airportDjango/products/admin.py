from django.contrib import admin
from products.models import *


@admin.register(Airlines)
class AirlinesAdmin(admin.ModelAdmin):
    list_display = ('nameAirlines', 'numberPhoneOne', 'website', 'email')
    ordering = ('nameAirlines',)
    search_fields = ('nameAirlines',)


@admin.register(TypeAirplanes)
class TypeAirplanesAdmin(admin.ModelAdmin):
    list_display = ('typeName', 'imgAirplane',)
    ordering = ('typeName',)
    search_fields = ('typeName',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('statusName',)
    ordering = ('statusName',)


@admin.register(Terminals)
class TerminalsAdmin(admin.ModelAdmin):
    list_display = ('terminalName',)
    ordering = ('terminalName',)


@admin.register(Airplanes)
class AirplanesAdmin(admin.ModelAdmin):
    list_display = ('flightNumber', 'scheduledDateDep', 'get_nameAirport', 'id_airlines', 'id_status', 'id_categoryFilters')
    list_editable = ('id_status',)
    ordering = ('flightNumber',)
    search_fields = ('flightNumber',)

    def get_nameAirport(self, obj):
        return obj.id_direction.nameAirport

    get_nameAirport.short_description = 'Направление (аэропорт)'


@admin.register(Directions)
class DirectionsAdmin(admin.ModelAdmin):
    list_display = ('nameAirport', 'city', 'IATA', 'ICAO', 'country', 'utc')
    ordering = ('city',)
    search_fields = ('city',)
