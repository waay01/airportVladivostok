from django.shortcuts import render
from products.models import Shops, Foods


def service(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
    ]

    context = {
        'css_file': 'service/css/styleService.css',
        'js_file': 'service/js/scriptsService.css',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/service.html', context)


def transport(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Транспорт', 'url': '/service/transport/'},
    ]

    context = {
        'css_file': 'transport/css/styleTransport.css',
        'js_file': 'transport/js/scriptsTransport.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/transport.html', context)


def luggage(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Багаж', 'url': '/service/luggage/'},
    ]

    context = {
        'css_file': 'luggage/css/styleLuggage.css',
        'js_file': 'luggage/js/scriptsLuggage.js',
        'breadcrumbs': breadcrumbs,
    }

    return render(request, 'service/luggage.html', context)


def foodRetail(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Еда и магазины', 'url': '/service/foodRetail/'},
    ]

    context = {
        'css_file': 'foodRetail/css/styleFoodRetail.css',
        'js_file': 'foodRetail/js/scriptsFoodRetail.js',
        'retailList': Shops.objects.all(),
        'foodList': Foods.objects.all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/foodRetail.html', context)


def baggageServices(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Упаковка и хранение багажа', 'url': '/service/baggageServices/'},
    ]

    context = {
        'css_file': 'baggageServices/css/styleBaggageServices.css',
        'js_file': 'baggageServices/js/scriptsBaggageServices.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/baggageServices.html', context)


def wifi(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Wi-Fi', 'url': '/service/wifi/'},
    ]

    context = {
        'css_file': 'wifi/css/styleWifi.css',
        'js_file': 'wifi/js/scriptsWifi.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/wifi.html', context)


def limitedMobility(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Маломобильные пассажиры', 'url': '/service/limitedMobility/'},
    ]

    context = {
        'css_file': 'limitedMobility/css/styleLimitedMobility.css',
        'js_file': 'limitedMobility/js/scriptsLimitedMobility.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/limitedMobility.html', context)


def childcareService(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Обслуживание пассажиров с детьми', 'url': '/service/childcareService/'},
    ]

    context = {
        'css_file': 'childcareService/css/styleChildcareService.css',
        'js_file': 'childcareService/js/scriptsChildcareService.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/childcareService.html', context)


def unaccompaniedMinors(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Обслуживание несопровождаемых детей', 'url': '/service/unaccompaniedMinors/'},
    ]

    context = {
        'css_file': 'unaccompaniedMinors/css/styleUnaccompaniedMinors.css',
        'js_file': 'unaccompaniedMinors/js/scriptsUnaccompaniedMinors.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/unaccompaniedMinors.html', context)


def transitAssistance(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Обслуживание транзитных и трансферных пассажиров', 'url': '/service/transitAssistance/'},
    ]

    context = {
        'css_file': 'transitAssistance/css/styleTransitAssistance.css',
        'js_file': 'transitAssistance/js/scriptsTransitAssistance.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/transitAssistance.html', context)


def medicalCare(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Медицинская помощь', 'url': '/service/medicalCare/'},
    ]

    context = {
        'css_file': 'medicalCare/css/styleMedicalCare.css',
        'js_file': 'medicalCare/js/scriptsMedicalCare.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/medicalCare.html', context)


def police(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Полиция', 'url': '/service/police/'},
    ]

    context = {
        'css_file': 'police/css/stylePolice.css',
        'js_file': 'police/js/scriptsPolice.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/police.html', context)


def emergencies(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Чрезвычайные ситуации', 'url': '/service/emergencies/'},
    ]

    context = {
        'css_file': 'emergencies/css/styleEmergencies.css',
        'js_file': 'emergencies/js/scriptsEmergencies.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/emergencies.html', context)


def inquiryServices(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Услуги информационной справочной', 'url': '/service/inquiryServices/'},
    ]

    context = {
        'css_file': 'inquiryServices/css/styleInquiryServices.css',
        'js_file': 'inquiryServices/js/scriptsInquiryServices.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/inquiryServices.html', context)


def eDeclaration(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Электронная таможенная декларация', 'url': '/service/eDeclaration/'},
    ]

    context = {
        'css_file': 'eDeclaration/css/styleEDeclaration.css',
        'js_file': 'eDeclaration/js/scriptsEDeclaration.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/eDeclaration.html', context)


def checkInServices(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Дополнительные услуги, оказываемые на стойках регистрации', 'url': '/service/checkInServices/'},
    ]

    context = {
        'css_file': 'checkInServices/css/styleCheckInServices.css',
        'js_file': 'checkInServices/js/scriptsCheckInServices.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/checkInServices.html', context)


def fastTrack(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Fast Track', 'url': '/service/fastTrack/'},
    ]

    context = {
        'css_file': 'fastTrack/css/styleFastTrack.css',
        'js_file': 'fastTrack/js/scriptsFastTrack.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/fastTrack.html', context)


def vipHall(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'VIP-зал', 'url': '/service/vipHall/'},
    ]

    context = {
        'css_file': 'vipHall/css/styleVipHall.css',
        'js_file': 'vipHall/js/scriptsVipHall.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/vipHall.html', context)


def waitingRoom(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Залы повышенной комфортности', 'url': '/service/waitingRoom/'},
    ]

    context = {
        'css_file': 'waitingRoom/css/styleWaitingRoom.css',
        'js_file': 'waitingRoom/js/scriptsWaitingRoom.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/waitingRoom.html', context)


def comfortableArea(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Зона комфортного ожидания', 'url': '/service/comfortableArea/'},
    ]

    context = {
        'css_file': 'comfortableArea/css/styleComfortableArea.css',
        'js_file': 'comfortableArea/js/scriptsComfortableArea.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/comfortableArea.html', context)


def motherChildRoom(request):
    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Услуги', 'url': '/service/'},
        {'text': 'Комната матери и ребенка', 'url': '/service/motherChildRoom/'},
    ]

    context = {
        'css_file': 'motherChildRoom/css/styleMotherChildRoom.css',
        'js_file': 'motherChildRoom/js/scriptsMotherChildRoom.js',
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'service/motherChildRoom.html', context)
