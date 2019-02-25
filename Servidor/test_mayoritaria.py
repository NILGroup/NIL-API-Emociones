import requests
from django.conf import settings

def mayoritaria(palabra):
        """
        Devuelve la emocion consensuada para una palabra.

        >>> mayoritaria("alegre")
        Mayoritaria: Alegría con un grado 4.83
        >>> mayoritaria("abandonado")
        Mayoritaria: Tristeza con un grado 4.3
        >>> mayoritaria("abeja")
        Mayoritaria: Miedo con un grado 3.53
        >>> mayoritaria("estafador")
        Mayoritaria: Ira con un grado 4.43
        >>> mayoritaria("acoso")
        Mayoritaria: Asco con un grado 4.07
        >>> mayoritaria("te")
        {'detail': 'Not found.'}
        """
        URL = settings.SITE_URL+'/emociones/' # URL del servidor
        sufijo = '/mayoritaria/' # sufijo de la consulta
        buscar = palabra
        buscada = buscar.lower()
        destino = URL+buscada+sufijo
        respuesta = requests.get(destino)
        mayoritaria = respuesta.json()
        print(mayoritaria)

if __name__ == "__main__":
        import doctest
        failure, test = doctest.testmod(verbose=True)
        if failure > 0:
                raise ValueError("TEST MAIN_EMOTION FAILED")
