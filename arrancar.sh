#!/bin/bash

python3 Servidor/manage.py runserver
#Servidor/tests.sh

# Nota: en producción, hay que llamar a manage.py con collectstatic y apuntar el
# servidor nginx o lo que sea para que sirva el directorio static.
