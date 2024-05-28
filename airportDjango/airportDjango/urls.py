"""
URL configuration for airportDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings as django_settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import *
from news.views import *
from service.views import *
from passengers.views import *
from scoreboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('settings/', settings, name='settings'),
    path('scoreboard/', scoreboard, name='scoreboard'),
    path('flight/<int:flight_id>/', flight, name='flight'),

    path('passengers/', passengers, name='passengers'),
    path('passengers/about/', about, name='about'),
    path('passengers/pressCenter/', pressCenter, name='pressCenter'),
    path('passengers/forMedia/', forMedia, name='forMedia'),
    path('passengers/career/', career, name='career'),
    path('passengers/airlines/', airlines, name='airlines'),
    path('passengers/contacts/', contacts, name='contacts'),
    path('passengers/mysteryPassenger/', mysteryPassenger, name='mysteryPassenger'),
    path('passengers/register/', register, name='register'),

    path('service/', service, name='service'),
    path('service/transport/', transport, name='transport'),
    path('service/luggage/', luggage, name='luggage'),
    path('service/foodRetail/', foodRetail, name='foodRetail'),
    path('service/baggageServices/', baggageServices, name='baggageServices'),
    path('service/wifi/', wifi, name='wifi'),
    path('service/limitedMobility/', limitedMobility, name='limitedMobility'),
    path('service/childcareService/', childcareService, name='childcareService'),
    path('service/unaccompaniedMinors/', unaccompaniedMinors, name='unaccompaniedMinors'),
    path('service/transitAssistance/', transitAssistance, name='transitAssistance'),
    path('service/medicalCare/', medicalCare, name='medicalCare'),
    path('service/police/', police, name='police'),
    path('service/emergencies/', emergencies, name='emergencies'),
    path('service/inquiryServices/', inquiryServices, name='inquiryServices'),
    path('service/eDeclaration/', eDeclaration, name='eDeclaration'),
    path('service/checkInServices/', checkInServices, name='checkInServices'),
    path('service/fastTrack/', fastTrack, name='fastTrack'),
    path('service/vipHall/', vipHall, name='vipHall'),
    path('service/waitingRoom/', waitingRoom, name='waitingRoom'),
    path('service/comfortableArea/', comfortableArea, name='comfortableArea'),
    path('service/motherChildRoom/', motherChildRoom, name='motherChildRoom'),

    path('news/', news, name='news'),
    path('news/<int:news_id>/', newsPage, name='newsPage'),
]

urlpatterns += static(django_settings.MEDIA_URL, document_root=django_settings.MEDIA_ROOT)
