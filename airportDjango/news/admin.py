from django.contrib import admin
from news.models import News, CarouselNews


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dateTime', 'author')
    ordering = ('dateTime',)
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(CarouselNews)
class CarouselNewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'showNews')
    list_editable = ('showNews',)

    def news_title(self, obj):
        return obj.news_id.title

    news_title.short_description = 'Заголовок новости'
