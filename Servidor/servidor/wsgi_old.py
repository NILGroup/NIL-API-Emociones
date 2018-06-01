"""
WSGI config for servidor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/tfgvr1718/TFG-1718-Emociones/Servidor')
#sys.path.append('/home/tfgvr1718/TFG-1718-Emociones/Servidor/entorno')

os.environ['DJANGO_SETTINGS_MODULE']="servidor.settings"
os.environ.setdefault("LANG", "en_US.UTF-8")
os.environ.setdefault("LC_ALL", "en_US.UTF-8")

#activate_this = '/home/tfgvr1718/TFG-1718-Emociones/Servidor/entorno/bin/activate.py'
#execfile(activate_this, dict(__file__=activate_this))

import site
site.addsitedir('/home/tfgvr1718/TFG-1718-Emociones/Servidor/entorno/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "servidor.settings")

application = get_wsgi_application()
