# NIL-API-Emociones

Servidor y API de análisis emocional del lenguaje natural.

## Contenidos

- `Servidor`: código y datos del servidor python+django.
- `Containerfile`: para el contenedor podman.
- `README.md`: Este fichero.
 
## Despliegue

Crear el contenedor (`podman build .`). Tras lanzarlo en el servidor, puede
ser necesario configurar el fichero `/app/servidor/settings.py`. También hay que
frontear los estáticos de `/app/static`. Se puede crear un volumen, o copiarlos
al host y frontearlos con Caddy p.ej.

## Créditos

Desarrollado para el trabajo de Fin de Grado titulado "Análisis Emocional para
la Inclusión Digital" y realizado por Elena Kaloyanova Popova, Gema Eugercios
Suárez y Paloma Gutiérrez Merino.

Actualizado por Antonio F. G. Sevilla <afgs@ucm.es>
