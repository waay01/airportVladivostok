# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/s/vladirr0/vladirr0.beget.tech/airportWebDjango')
sys.path.insert(1, '/home/s/vladirr0/vladirr0.beget.tech/venv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'airportWebDjango.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()