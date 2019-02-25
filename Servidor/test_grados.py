import requests
from django.conf import settings

def porcentajes(palabra):
        """
        Devuelve los porcentajes de emocion para una palabra.

        >>> porcentajes("alegre")
        Tristeza:1.1 || Miedo:1.23 || Alegría:4.83 || Ira:1.1 || Asco:1.03
        >>> porcentajes("araña")
        Tristeza:1.5 || Miedo:3.53 || Alegría:1.17 || Ira:2.33 || Asco:3.77
        >>> porcentajes("corazón")
        Tristeza:1.73 || Miedo:1.57 || Alegría:3.43 || Ira:1.4 || Asco:1.37
        >>> porcentajes("te")
        {'detail': 'Not found.'}
        """
        URL = settings.SITE_URL+'/emociones/' # URL del servidor
        sufijo = '/grados/' # sufijo de la consulta
        buscada = palabra.lower()
        destino = URL+buscada+sufijo
        respuesta = requests.get(destino)
        porcentajes = respuesta.json()
        print(porcentajes)

if __name__ == "__main__":
        import doctest
        failure, test = doctest.testmod(verbose=True)
        if failure > 0:
                raise ValueError("TEST PERCENTAGES FAILED")
