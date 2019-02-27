#!/bin/bash
# Script que crea un contenedor e instala en su interior el proyecto listo para
# ser arrancado

rm -rf ./extra/Servidor
mkdir -p ./extra/Servidor
git --work-tree=./extra/ checkout HEAD -- Servidor
mkosi -f \
    --with-network \
    --distribution debian \
    --release testing \
    --mirror 'http://ftp.es.debian.org/debian/' \
    --format directory \
    --extra-tree extra \
    --postinst-script install.sh \
    --output emociones-contenedor
