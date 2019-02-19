import requests
from interprete_frases import InterpreteFrases
from salida import Salida

def frases(frase):
        """
        Devuelve los grados de emocion para una palabra.

        >>> frases("Ana está triste y avergonzada")
        Lista de palabras emocionales:
        ['triste', 'avergonzada']
        Grado de tristeza: 3.75
        Grado de miedo: 2.58
        Grado de alegria: 1.11
        Grado de ira: 2.2
        Grado de asco: 1.55
        La mayoritaria es Tristeza con un grado 3.75
        >>> frases("Llevaba una escopeta")
        Lista de palabras emocionales:
        ['Llevaba', 'escopeta']
        Grado de tristeza: 2.33
        Grado de miedo: 3.63
        Grado de alegria: 1.23
        Grado de ira: 2.8
        Grado de asco: 2.06
        La mayoritaria es Miedo con un grado 3.63
        >>> frases("Estoy alegre y feliz")
        Lista de palabras emocionales:
        ['alegre', 'feliz']
        Grado de tristeza: 1.1
        Grado de miedo: 1.21
        Grado de alegria: 4.73
        Grado de ira: 1.05
        Grado de asco: 1.02
        La mayoritaria es Alegría con un grado 4.73
        >>> frases("Ese tipo es un arrogante")
        Lista de palabras emocionales:
        ['tipo', 'arrogante']
        Grado de tristeza: 2.27
        Grado de miedo: 1.63
        Grado de alegria: 1.0
        Grado de ira: 3.27
        Grado de asco: 3.03
        La mayoritaria es Ira con un grado 3.27
        >>> frases("Aquí hay muchos cotilleos")
        Lista de palabras emocionales:
        ['cotilleos']
        Grado de tristeza: 1.63
        Grado de miedo: 1.63
        Grado de alegria: 1.97
        Grado de ira: 1.97
        Grado de asco: 2.06
        La mayoritaria es Asco con un grado 2.06
        >>> frases("Hola Juan")
        Lista de palabras emocionales:
        []
        Grado de tristeza: 1
        Grado de miedo: 1
        Grado de alegria: 1
        Grado de ira: 1
        Grado de asco: 1
        >>> frases("Ana está triste porque se ha roto su ascensor")
        Lista de palabras emocionales:
        ['triste', 'roto', 'ascensor']
        Grado de tristeza: 3.06
        Grado de miedo: 2.16
        Grado de alegria: 1.22
        Grado de ira: 2.15
        Grado de asco: 1.32
        La mayoritaria es Tristeza con un grado 3.06
        """
        interpreta = InterpreteFrases()
        _salida = Salida()
        grados,palabras = interpreta.emociones_frase(frase)
        _salida.mostrar_palabras(palabras)
        _salida.mostrar_grados(grados)
        if len(palabras) > 0:
                mayoritarias,porcentaje = interpreta.emocion_mayoritaria_frase(grados)
                _salida.mostrar_mayoritaria(mayoritarias,porcentaje)

if __name__ == "__main__":
        import doctest
        failure, test = doctest.testmod(verbose=True)
        if failure > 0:
                raise ValueError("TEST SENTENCES FAILED")
