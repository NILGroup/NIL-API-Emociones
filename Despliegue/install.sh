#!/bin/bash
# Script que instala las dependencias del proyecto

# Instalar dependencias de aptitude
apt install -y python3 python3-pip python3-setuptools \
    python3-wheel build-essential python3-dev \
    nginx

# Instalar dependencias python
pip3 install django \
            djangorestframework \
            requests \
            cython \
            pystemmer \
            spacy

# Descargar el modelo de spacy
python3 -m spacy download es

# Instalar la configuración para nginx
rm -f /etc/nginx/sites-enabled/*
ln -s /etc/nginx/sites-available/emociones /etc/nginx/sites-enabled/emociones

# Ejecutar migraciones de django y preparar los estáticos
cd /Servidor
python3 manage.py migrate
python3 manage.py collectstatic

# Activar los servicios necesarios para que arranquen con el contenedor
systemctl enable nginx emociones systemd-networkd systemd-resolved
