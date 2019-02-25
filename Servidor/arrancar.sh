#!/bin/bash

python3 manage.py runserver
#Servidor/tests.sh

# Nota: en producción, hay que llamar a manage.py con collectstatic y apuntar el
# servidor nginx o lo que sea para que sirva el directorio static.
