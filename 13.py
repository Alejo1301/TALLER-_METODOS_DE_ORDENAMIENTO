# Lista de números aleatorios: Genera una lista de 20 números aleatorios y ordénalos con el
# algoritmo de mergesort


import random

def mergesort_numeros(numeros):
    if len(numeros) <= 1:
        return numeros
    mitad = len(numeros) // 2
    izquierda = mergesort_numeros(numeros[:mitad])
    derecha = mergesort_numeros(numeros[mitad:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    while len(izquierda) > 0 and len(derecha) > 0:
        if izquierda[0] <= derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    resultado.extend(izquierda)
    resultado.extend(derecha)
    return resultado

# Genera una lista de 20 números aleatorios
numeros = [random.randint(1, 100) for _ in range(20)]

print("Números aleatorios originales:")
print(numeros)

print("Números aleatorios ordenados con mergesort:")
print(mergesort_numeros(numeros))



#Por burbuja


import random

def burbuja_numeros(numeros):
    n = len(numeros)
    for i in range(n-1):
        for j in range(n-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    return numeros

# Genera una lista de 20 números aleatorios
numeros = [random.randint(1, 100) for _ in range(20)]

print("Números aleatorios :")
print(numeros)

print("Números aleatorios ordenados con el método burbuja:")
print(burbuja_numeros(numeros))