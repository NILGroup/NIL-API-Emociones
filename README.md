# NIL-API-Emociones

Servidor y API de análisis emocional del lenguaje natural.

## Contenidos

- `Servidor`: código y datos del servidor python+django.
- `Despliegue`: Ficheros necesarios para el despliegue e instalación.
- `README.md`: Este fichero.
 
## Instalación

Antes de instalar, puede ser necesario configurar el fichero
`Servidor/servidor/settings.py`.

### Como proceso local

Crear un entorno virtual, por ejemplo con conda, y ejecutar el script de
instalación como usuario no root:

```sh
$ conda create -n emociones
$ source activate emociones
$ ./Despliegue/install.sh
```

Para lanzar el servidor:

```sh
$ source activate emociones
$ cd Servidor && ./arrancar.sh
```

**Nota**: Para este uso, mejor utilizar `DEBUG=True` en `settings.py`.

### Como root

Recomendado para ejecución en un contenedor, por ejemplo creado con `mkosi` y
gestionado con `systemd-nspawn`. Instala todas las dependencias a nivel de
sistema, despliega en el path absoluto `"/Servidor"`, prepara un servidor nginx
y habilita los servicios `systemd` necesarios para que la api se arranque
automáticamente con el servidor.

Tras crear el contenedor, copiar el repositorio a la raíz de éste. Desde dentro
del contenedor:

```sh
# cd /
# /Despliegue/install.sh
```

## Créditos

Desarrollado para el trabajo de Fin de Grado titulado "Análisis Emocional para
la Inclusión Digital" y realizado por Elena Kaloyanova Popova, Gema Eugercios
Suárez y Paloma Gutiérrez Merino.

Actualizado por Antonio F. G. Sevilla <afgs@ucm.es>
