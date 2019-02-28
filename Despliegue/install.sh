#!/bin/bash
#
# Script que instala en una máquina el servidor y lo prepara para ejecutar.
#
# Hay dos opciones, instalar con sudo o root, o como usuario normal.
#
# ## Instalación como root
#
# Se instalan las dependencias necesarias, los ficheros de configuración, y
# activan los servicios.
#
# **¡Atención!** Se desactivan todos los servidores nginx previos, si se quiere
# compartir la instancia nginx hay que cambiar después la configuración a mano.
#
# ## Instalación como usuario local
#
# Se instalan con sudo las dependencias de apt, y sin sudo las de python. Se
# recomienda activar primero un entorno virtual venv o conda. No se instala
# nginx, por lo que si se quiere usar hay que hacerlo a mano, usar como
# inspiración el fichero del directorio Despliegue.

DEPENDENCIAS="python3 python3-pip python3-setuptools python3-wheel build-essential python3-dev nginx"
PAQUETES_PIP="django djangorestframework requests cython pystemmer spacy"

if [ "$EUID" -eq 0 ]; then
    # Como root
    echo "Instalando como ROOT"
    COMO_ROOT=1
    PATH_SERVIDOR="/Servidor"
    apt install -y $DEPENDENCIAS
    PYTHON=python3
    PIP=pip3
else
    # Usuario local
    echo "Instalando como usuario local"
    COMO_ROOT=0
    PATH_SERVIDOR="$PWD/Servidor"
    sudo apt install $DEPENDENCIAS
    PYTHON=python
    PIP=pip
fi

# Instalar dependencias python
$PIP install $PAQUETES_PIP

# Descargar el modelo de spacy
$PYTHON -m spacy download es

# Ejecutar migraciones de django, preparar los estáticos, cargar palabras en la
# base de datos
pushd $PATH_SERVIDOR
$PYTHON manage.py migrate
$PYTHON manage.py collectstatic --clear --noinput
$PYTHON fichero.py
popd

if [ "$COMO_ROOT" -ne 1 ]; then exit 0; fi

# Instalar la configuración para nginx
rm -f /etc/nginx/sites-enabled/*
cp Despliegue/emociones.nginx /etc/nginx/sites-available/emociones.nginx
ln -s /etc/nginx/sites-available/emociones.nginx /etc/nginx/sites-enabled/emociones.nginx

# Instalar el servico de systemd
cp Despliegue/emociones.service /etc/systemd/system/emociones.service

# Activar los servicios necesarios para que arranquen con el contenedor
systemctl enable nginx emociones systemd-networkd systemd-resolved
