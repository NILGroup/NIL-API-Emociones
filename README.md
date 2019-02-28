# NIL-API-Emociones

Servidor y API de análisis emocional del lenguaje natural.

## Contenidos

- `Servidor`: código y datos del servidor python+django.
- `Despliegue`: Ficheros necesarios para el despliegue e instalación.
- `README.md`: Este fichero.
 
## Uso

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

### Como contenedor

Para crear un contenedor con el servidor de manera automática, instalar la
herramienta `mkosi` y ejecutar en este directorio:

```sh
$ sudo mkosi -f --default=Despliegue/mkosi.default
```

El contenedor se crea por defecto en `/var/lib/machines`, por lo que se puede
lanzar usando:

```sh
$ sudo systemd-nspawn -nb -M emociones-contenedor
```

## Créditos

Desarrollado para el trabajo de Fin de Grado titulado "Análisis Emocional para
la Inclusión Digital" y realizado por Elena Kaloyanova Popova, Gema Eugercios
Suárez y Paloma Gutiérrez Merino.

Actualizado por Antonio F. G. Sevilla <afgs@ucm.es>
