from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    shortDescription = models.TextField(verbose_name="Описание")
    description = models.TextField(verbose_name="Описание")
    imgPoster = models.ImageField(verbose_name="Фото", upload_to='news')
    dateTime = models.DateTimeField(verbose_name="Дата/Время", default=timezone.now)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class CarouselNews(models.Model):
    SHOW = 'SHOW'
    HIDE = 'HIDE'
    CURRENT_CHOICE = [
        (SHOW, 'Показать'),
        (HIDE, 'Скрыть')
    ]

    news_id = models.ForeignKey(News, on_delete=models.PROTECT, verbose_name="Новость")
    showNews = models.CharField(verbose_name="Показать новость", choices=CURRENT_CHOICE, max_length=8)

    def __str__(self):
        return self.news_id.title

    class Meta:
        verbose_name = "Карусель новостей"
        verbose_name_plural = "Карусель новостей"
