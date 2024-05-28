from django.contrib import admin
from news.models import *


# добавить автора поста для обычных новостей

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dateTime',)
    ordering = ('dateTime',)
    search_fields = ('title',)


class CarouselImageAdmin(admin.TabularInline):
    model = CarouselImage
    extra = 0


@admin.register(CarouselNews)
class CarouselNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'showNews', 'imgPoster')
    list_editable = ('showNews',)
    inlines = [CarouselImageAdmin]
