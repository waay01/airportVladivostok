from django.db import models


class Places(models.Model):
    placeName = models.CharField(verbose_name="Расположение места", max_length=255)

    def __str__(self):
        return self.placeName

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Shops(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    timeWork = models.CharField(verbose_name="Время работы", max_length=255)
    id_place = models.ForeignKey(to='Places', on_delete=models.PROTECT, verbose_name="Место")
    imgPoster = models.ImageField(verbose_name="Фото", upload_to='shops')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"


class Foods(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    timeWork = models.CharField(verbose_name="Время работы", max_length=255)
    id_place = models.ForeignKey(to='Places', on_delete=models.PROTECT, verbose_name="Место")
    imgPoster = models.ImageField(verbose_name="Фото", upload_to='foods')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Еда"
        verbose_name_plural = "Еда"
