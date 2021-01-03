from numpy.random import RandomState


def leer_test(path):
    """ Retorna un test del problema de la mochila.

    Parameters
    ----------
    path : str
        Direccion relativa a el test
    Returns
    -------
    list
        Lista con los datos del problema.
    """

    data = []
    with open(path) as f:
        next(f)
        n = int(f.readline().split()[1])
        c = int(f.readline().split()[1])
        z = int(f.readline().split()[1])
        data.extend((n, c, z))
        for line in f.readlines()[1:]:
            data.append([int(x) for x in line.split(",")[1:3]])
    return data


def seleccion_ruleta(poblacion, probabilidades, n, prng):
    """ Retorna una cantidad n de individuos desde una poblacion en forma aleatorea.

    Parameters
    ----------
    poblacion : list
        Elementos de la poblacion.
    probabilidades : list
        Probabilidades respectivas a los elementos de poblacion.
    n : int
        Numero de individuos a obtener desde la ruleta.
    prng : RandomState
        Generador de numeros pseudoaleatoreos.
    Returns
    -------
    list
        Listado de individuos.
    """

    seleccionados = []
    for _ in range(n):
        r = prng.rand()
        for (i, individuo) in enumerate(poblacion):
            if r <= probabilidades[i]:
                seleccionados.append(individuo)
                break
    return seleccionados


def obtener_elementos(solucion, fitness, condicion):
    """ Retorna una lista de los elementos que cumplan una cierta condicion

    Parameters
    ----------
    solucion : list
        Lista que representa los elementos a incluir en la mochila.
    fitness : list
        Lista con el fitness para cada elemento de la solucion.
    condicion : int
        Entero que debe ser igual a los elementos en la lista solucion.

    Returns
    -------
    list
        Una lista de tuplas con el indice y el fitness del elemento.
    """

    muestra = []
    for idx in range(len(solucion)):
        if solucion[idx] == condicion:
            muestra.append((idx, fitness[idx]))
    return muestra
