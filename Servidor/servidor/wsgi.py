"""
WSGI config for servidor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

os.environ['DJANGO_SETTINGS_MODULE']="servidor.settings"
os.environ.setdefault("LANG", "en_US.UTF-8")
os.environ.setdefault("LC_ALL", "en_US.UTF-8")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
