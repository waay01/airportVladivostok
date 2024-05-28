from django.db import models


class CarouselNews(models.Model):
    SHOW = 'SHOW'
    HIDE = 'HIDE'
    CURRENT_CHOICE = [
        (SHOW, 'Показать'),
        (HIDE, 'Скрыть')
    ]

    title = models.CharField(verbose_name="Заголовок", max_length=255)
    description = models.TextField(verbose_name="Описание")
    showNews = models.CharField(verbose_name="Показать новость", choices=CURRENT_CHOICE, max_length=8)
    imgPoster = models.ImageField(verbose_name="Фото", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карусель новостей"
        verbose_name_plural = "Карусель новостей"


class CarouselImage(models.Model):
    carousel = models.ForeignKey(CarouselNews, on_delete=models.PROTECT, verbose_name="Карусель")
    image = models.ImageField(verbose_name="Фото", upload_to='carousel News')

    def __str__(self):
        return self.carousel

    class Meta:
        verbose_name = "Карусель новостей(фото)"
        verbose_name_plural = "Карусель новостей(фото)"


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    description = models.TextField(verbose_name="Описание")
    dateTime = models.DateTimeField(verbose_name="Дата/Время")
    # author = models.CharField(verbose_name="Автор", max_length=255) Сделать чтоб логин автоматически брался и был не изменяемый
    imgPoster = models.ImageField(verbose_name="Фото", upload_to='news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
