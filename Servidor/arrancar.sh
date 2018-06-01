#!/bin/bash
source Servidor/entorno/bin/activate
gnome-terminal -x bash -c "python3 Servidor/manage.py runserver"
Servidor/tests.sh