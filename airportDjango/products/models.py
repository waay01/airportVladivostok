from django.db import models
from django.utils import timezone


# Билеты, самолет

class Airlines(models.Model):
    nameAirlines = models.CharField(verbose_name="Название авиакомпании", max_length=255)
    numberPhoneOne = models.CharField(verbose_name="Номер телефона", max_length=20)
    numberPhoneTwo = models.CharField(verbose_name="Номер телефона", max_length=20, null=True, blank=True)
    website = models.URLField(verbose_name="Сайт", null=True, blank=True)
    email = models.EmailField(verbose_name="Почта", null=True, blank=True)
    logoBig = models.ImageField(verbose_name="Большой логотип", upload_to='logo Airlines')
    logoSmall = models.ImageField(verbose_name="Маленький логотип", upload_to='logo Airlines', null=True, blank=True)

    def __str__(self):
        return self.nameAirlines

    class Meta:
        verbose_name = "Авиакомпания"
        verbose_name_plural = "Авиакомпании"


class TypeAirplanes(models.Model):
    typeName = models.CharField(verbose_name="Название модели", max_length=255)
    imgAirplane = models.ImageField(verbose_name="Фотография самолета", upload_to='type Airplanes')

    def __str__(self):
        return self.typeName

    class Meta:
        verbose_name = "Модель самолета"
        verbose_name_plural = "Модели самолетов"


# мб переделать, убрать таблицу и сделать через Choice
class Status(models.Model):
    statusName = models.CharField(verbose_name="Статус", max_length=255)

    def __str__(self):
        return self.statusName

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Terminals(models.Model):
    terminalName = models.CharField(verbose_name="Терминал", max_length=255)

    def __str__(self):
        return self.terminalName

    class Meta:
        verbose_name = "Терминал"
        verbose_name_plural = "Терминалы"


class Airplanes(models.Model):
    ARRIVAL = 'ARR'
    DEPARTURE = 'DEP'
    CURRENT_CHOICE = [
        (ARRIVAL, 'Прибытие'),
        (DEPARTURE, 'Отправление')
    ]

    scheduledDateDep = models.DateTimeField(verbose_name="Запланированная время/дата вылета")
    expectedDateDep = models.DateTimeField(verbose_name="Фактическая дата время/вылета", null=True, blank=True)
    scheduledDateArr = models.DateTimeField(verbose_name="Запланированная время/дата прилета")
    expectedDateArr = models.DateTimeField(verbose_name="Фактическая дата время/прилета", null=True, blank=True)
    id_typeAirplane = models.ForeignKey(to='TypeAirplanes', on_delete=models.PROTECT, verbose_name="Модель самолета")
    id_direction = models.ForeignKey(to='Directions', on_delete=models.PROTECT, verbose_name="Направление (аэропорт)")
    id_airlines = models.ForeignKey(to='Airlines', on_delete=models.PROTECT, verbose_name="Авиакомпания")
    flightNumber = models.CharField(verbose_name="Номер рейса", max_length=255)
    id_terminal = models.ForeignKey(to='Terminals', on_delete=models.PROTECT, verbose_name="Терминал")
    receptionDesks = models.CharField(verbose_name="Стойка(и) регистрации", max_length=255, null=True, blank=True)
    gate = models.CharField(verbose_name="Выход", max_length=8, null=True, blank=True)
    id_status = models.ForeignKey(to='Status', on_delete=models.PROTECT, verbose_name="Статус")
    id_categoryFilters = models.CharField(verbose_name="Фильтр", max_length=6, choices=CURRENT_CHOICE)

    def __str__(self):
        return self.flightNumber

    class Meta:
        verbose_name = "Самолет"
        verbose_name_plural = "Самолеты"


class Directions(models.Model):
    country = models.CharField(verbose_name="Страна", max_length=255)
    city = models.CharField(verbose_name="Город", max_length=255)
    nameAirport = models.CharField(verbose_name="Аэропорт", primary_key=True, unique=True, max_length=255)
    utc = models.IntegerField(verbose_name="Часовой пояс (UTC)")
    IATA = models.CharField(verbose_name="IATA код", unique=True, max_length=255)
    ICAO = models.CharField(verbose_name="ICAO код", unique=True, max_length=255)
    coordinates = models.CharField(verbose_name="Координаты", max_length=255)

    def save(self, *args, **kwargs):
        self.nameAirport = self.nameAirport.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nameAirport

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
