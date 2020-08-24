"""
WSGI config for data_collector project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_collector.settings")

application = Cling(get_wsgi_application())

# whitenoise用に追加
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)


