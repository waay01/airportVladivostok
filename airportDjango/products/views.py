from datetime import datetime, timedelta

from django.http import JsonResponse
from django.shortcuts import render
# Ключи
from keys import *
from news.models import CarouselNews
from products.models import Airplanes


# основа
def index(request):
    context = {
        'css_file': 'index/css/styleIndex.css',
        'js_file': 'index/js/scriptsIndex.js',
        'airplanesDepCount': Airplanes.objects.filter(id_categoryFilters='DEP').count,
        'airplanesArrCount': Airplanes.objects.filter(id_categoryFilters='ARR').count,
        'carouselNewsList': CarouselNews.objects.all(),
    }
    return render(request, 'products/index.html', context)


def settings(request):
    context = {
        'css_file': 'settings/css/styleSettings.css',
        'js_file': 'settings/js/scriptsSettings.js',
    }
    return render(request, 'products/settings.html', context)


def scoreboard(request):
    flight_type = request.GET.get('type', '')

    try:
        date = request.GET.get('date')
    except ValueError:
        date = datetime.now().strftime('%Y-%m-%d')

    if key_calcDateFlights == 1:
        yesterday = datetime.now().date() - timedelta(days=1)
        tomorrow = datetime.now().date() + timedelta(days=1)
        airplanesDateList = [yesterday, datetime.now().date(), tomorrow]
    elif key_calcDateFlights == 2:
        airplanesDateList = Airplanes.objects.values_list('scheduledDateDep', flat=True).filter(id_categoryFilters=flight_type).distinct()

    notification = Airplanes.objects.filter(id_status_id__in=[3, 10]).exists()

    context = {
        'css_file': 'scoreboard/css/styleScoreboard.css',
        'js_file': 'scoreboard/js/scriptsScoreboard.js',
        'airplanesList': Airplanes.objects.filter(id_categoryFilters=flight_type),
        'DateList': airplanesDateList,
        'notification': notification,
    }

    return render(request, 'products/scoreboard.html', context)


def flight(request, flight_id):
    try:
        airplane = Airplanes.objects.get(id=flight_id)

        scheduled_datetime_dep = datetime.combine(airplane.scheduledDateDep, airplane.scheduledTimeDep)

        # Прибытие в аэропорт
        new_TFP = scheduled_datetime_dep - timedelta(hours=2.5)
        timeForPassing = new_TFP.strftime("%H:%M")  # Отвечает за прибытие к аэропорту за 2.5 часа

        # Регистрация
        new_TR = scheduled_datetime_dep - timedelta(hours=1.33)
        timeRegister = new_TR.strftime("%H:%M")  # Отвечает за регистрацию за 40 минут

        # Посадка в самолет
        new_TFL = scheduled_datetime_dep - timedelta(hours=1)
        timeForLand = new_TFL.strftime("%H:%M")  # Отвечает за посадку в самолет за 1 час

        # Время вылета
        new_TO = scheduled_datetime_dep + timedelta(hours=0.25)
        timeTakeoff = new_TO.strftime("%H:%M")

        if key_calcTimeSubScheduled:
            scheduled_datetime_dep = datetime.combine(airplane.scheduledDateDep, airplane.scheduledTimeDep)
            scheduled_datetime_arr = datetime.combine(airplane.scheduledDateArr, airplane.scheduledTimeArr)
        elif not key_calcTimeSubScheduled:
            expected_datetime_dep = datetime.combine(airplane.expectedDateDep, airplane.expectedTimeDep)
            expected_datetime_arr = datetime.combine(airplane.expectedDateArr, airplane.expectedTimeArr)

        # expected_datetime_arr = datetime.combine(airplane.expectedDateArr, airplane.expectedTimeArr, tzinfo=timezone_arr)

        # Расчет разницы во времени с учетом часовых поясов
        if key_calcTimeSubScheduled:
            new_TS = scheduled_datetime_arr - scheduled_datetime_dep
        elif not key_calcTimeSubScheduled:
            new_TS = expected_datetime_arr - expected_datetime_dep

        airplanes = Airplanes.objects.filter(id=flight_id)
        context = {
            'css_file': 'flight/css/styleFlight.css',
            'js_file': 'flight/js/scriptsFlight.js',
            'airplanesList': airplanes,
            'timeForPassing': timeForPassing,
            'timeRegister': timeRegister,
            'timeForLand': timeForLand,
            'timeTakeoff': timeTakeoff,
            'timeSub': new_TS,
        }
        return render(request, 'products/flight.html', context)
    except Airplanes.DoesNotExist:
        return JsonResponse({'error': 'flight is delete'}, status=404)


# passengers
def about(request):
    context = {
        'css_file': 'about/css/styleAbout.css',
        'js_file': 'about/js/scriptsAbout.js',
    }
    return render(request, 'products/about.html', context)


def pressCenter(request):
    context = {
        'css_file': 'pressCenter/css/stylePressCenter.css',
        'js_file': 'pressCenter/js/scriptsPressCenter.js',
    }

    return render(request, 'products/pressCenter.html', context)


def forMedia(request):
    context = {
        'css_file': 'forMedia/css/styleForMedia.css',
        'js_file': 'forMedia/js/scriptsForMedia.js',
    }

    return render(request, 'products/forMedia.html', context)


def career(request):
    context = {
        'css_file': 'career/css/styleCareer.css',
        'js_file': 'career/js/scriptsCareer.js',
    }

    return render(request, 'products/career.html', context)


def contacts(request):
    context = {
        'css_file': 'contacts/css/styleContacts.css',
        'js_file': 'contacts/js/scriptsContacts.js',
    }

    return render(request, 'products/contacts.html', context)


def airlines(request):
    context = {
        'css_file': 'airlines/css/styleAirlines.css',
        'js_file': 'airlines/js/scriptsAirlines.js',
    }

    return render(request, 'products/airlines.html', context)


def mysteryPassenger(request):
    context = {
        'css_file': 'mysteryPassenger/css/styleMysteryPassenger.css',
        'js_file': 'mysteryPassenger/js/scriptsMysteryPassenger.js',
    }

    return render(request, 'products/mysteryPassenger.html', context)


def register(request):
    context = {
        'css_file': 'register/css/styleRegister.css',
        'js_file': 'register/js/scriptsRegister.js',
    }

    return render(request, 'products/register.html', context)


def passengers(request):
    return about(request)
