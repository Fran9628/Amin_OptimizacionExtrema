import sys
import time
import numpy as np
from funciones import leer_test, seleccion_ruleta, obtener_elementos
from numpy.random import RandomState


def main(tau, max_it, data, prng):
    # Mochila (n, c, z, elementos y fitness)
    n = int(data[0])
    capacidad = int(data[1])
    optimo = int(data[2])
    elementos = data[3:]  # (valor, peso)
    fitness = [e[0] / e[1] for e in elementos]

    # Solucion inicial mochila llena
    solucion = np.ones(n)
    valor = sum(x[0] for x in elementos)
    peso = sum(x[1] for x in elementos)
    print(valor, peso)

    # Valores probabilidades
    p = [(i + 1) ** tau for i in range(n)]
    acumulado = [sum(p[:i + 1]) for i in range(n)]

    # Algoritmo
    for it in range(max_it):
        # Condicion de termino
        if valor == optimo:
            print(f"Solucion encontrada #{it}!\nValor: {valor}\nPeso: {peso}")
            print(solucion)
            break

        # Remover o agregar un elemento
        if peso >= capacidad:
            muestra = obtener_elementos(solucion, fitness, 1)
            ordenada = sorted(muestra, key=lambda x: x[1])
            divisor = acumulado[len(ordenada) - 1]
            proporcion = [(i + 1) / divisor for i in range(len(ordenada))]
            sumatoria = [sum(proporcion[:x+1]) for x in range(len(proporcion))]
            seleccion = seleccion_ruleta(ordenada, sumatoria, 1, prng)
            idx = seleccion[0][0]
            solucion[idx] = 0
            valor -= elementos[idx][0]
            peso -= elementos[idx][1]
            if valor < 0:
                valor = 0
            if peso < 0:
                peso = 0
        else:
            muestra = obtener_elementos(solucion, fitness, 0)
            ordenada = sorted(muestra, key=lambda x: x[1], reverse=True)
            divisor = acumulado[len(ordenada) - 1]
            proporcion = [(i + 1) / divisor for i in range(len(ordenada))]
            sumatoria = [sum(proporcion[:x+1]) for x in range(len(proporcion))]
            seleccion = seleccion_ruleta(ordenada, sumatoria, 1, prng)
            idx = seleccion[0][0]
            solucion[idx] = 1
            valor += elementos[idx][0]
            peso += elementos[idx][1]
        # print(it)


if __name__ == '__main__':
    # python eo.py -1.4 100000 test.csv 1
    if len(sys.argv) > 1:
        tau = float(sys.argv[1])
        max_it = int(sys.argv[2])
        data = leer_test(sys.argv[3])
        if len(sys.argv) > 4:
            prng = RandomState(int(sys.argv[4]))
        else:
            prng = RandomState()
    else:
        tau = -1.4
        max_it = 100000
        data = leer_test("test.csv")
        prng = RandomState(22000)
    start_time = time.time()
    main(tau, max_it, data, prng)
    print("Tiempo de ejecucion:", time.time() - start_time)
