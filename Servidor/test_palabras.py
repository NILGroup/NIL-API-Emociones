import requests
from interprete_palabras import InterpretePalabras
from salida import Salida

def palabras(op,palabra):
        """
        Pruebas sobre el interprete de palabras

        >>> palabras(0,"alegre")
        Grado de tristeza: 1.1
        Grado de miedo: 1.23
        Grado de alegria: 4.83
        Grado de enfado: 1.1
        Grado de asco: 1.03
        >>> palabras(0,"araña")
        Grado de tristeza: 1.5
        Grado de miedo: 3.53
        Grado de alegria: 1.17
        Grado de enfado: 2.33
        Grado de asco: 3.77
        >>> palabras(0,"corazón")
        Grado de tristeza: 1.73
        Grado de miedo: 1.57
        Grado de alegria: 3.43
        Grado de enfado: 1.4
        Grado de asco: 1.37
        >>> palabras(0,"te")
        No se ha encontrado la palabra. Asegurese de haberla escrito bien.

        >>> palabras(1,"alegre")
        No hay emocion consensuada.
        >>> palabras(1,"diamante")
        No hay emocion consensuada.
        >>> palabras(1,"te")
        No se ha encontrado la palabra. Asegurese de haberla escrito bien.

        >>> palabras(2,"alegre")
        La mayoritaria es Alegría con un grado 4.83
        >>> palabras(2,"abandonado")
        La mayoritaria es Tristeza con un grado 4.3
        >>> palabras(2,"abeja")
        La mayoritaria es Miedo con un grado 3.53
        >>> palabras(2,"estafador")
        La mayoritaria es Ira con un grado 3.17
        >>> palabras(2,"acoso")
        La mayoritaria es Asco con un grado 4.07
        >>> palabras(2,"te")
        No se ha encontrado la palabra. Asegurese de haberla escrito bien.
        """
        interpreta = InterpretePalabras()
        _salida = Salida()
        if op == 0:
                porcentajes = interpreta.interpretar_grados(palabra)
                _salida.mostrar_porcentajes(porcentajes)
        elif op == 1:
                consensuada = interpreta.interpretar_consensuada(palabra)
                _salida.mostrar_consensuada(consensuada)
        elif op == 2:
                mayoritarias,porcentaje = interpreta.interpretar_mayoritaria(palabra)
                _salida.mostrar_mayoritaria(mayoritarias,porcentaje)

if __name__ == "__main__":
        import doctest
        failure, test = doctest.testmod(verbose=True)
        if failure > 0:
                raise ValueError("TEST WORDS FAILED")
