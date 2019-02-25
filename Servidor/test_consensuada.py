import requests
from django.conf import settings

def consensuada(palabra):
        """
        Devuelve la emocion consensuada para una palabra.

        >>> consensuada("alegre")
        No hay emocion consensuada
        >>> consensuada("araña")
        No hay emocion consensuada
        >>> consensuada("corazón")
        No hay emocion consensuada
        >>> consensuada("te")
        {'detail': 'Not found.'}
        """
        URL = settings.SITE_URL+'/emociones/' # URL del servidor
        sufijo = '/consensuada/' # sufijo de la consulta
        buscar = palabra
        buscada = buscar.lower()
        destino = URL+buscada+sufijo
        respuesta = requests.get(destino)
        consensuada = respuesta.json()
        print(consensuada)

if __name__ == "__main__":
        import doctest
        failure, test = doctest.testmod(verbose=True)
        if failure > 0:
                raise ValueError("TEST AGREED_EMOTION FAILED")
