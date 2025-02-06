
# . Ordenación de puntajes deportivos: Ordena una lista de puntajes deportivos utilizando el método
# de quicksort

def quicksort_puntajes(puntajes):
    if len(puntajes) <= 1:
        return puntajes
    pivote = puntajes[len(puntajes) // 2]
    izquierda = [x for x in puntajes if x < pivote]
    medio = [x for x in puntajes if x == pivote]
    derecha = [x for x in puntajes if x > pivote]
    return quicksort_puntajes(izquierda) + medio + quicksort_puntajes(derecha)


puntajes = [78, 56, 79, 23, 90, 14, 67, 90]
print("Puntajes originales:", puntajes)
print("Puntajes ordenados:", quicksort_puntajes(puntajes))

#por burbuja

def burbuja_puntajes(puntajes):
    n = len(puntajes)
    for i in range(n-1):
        for j in range(n-i-1):
            if puntajes[j] > puntajes[j+1]:
                puntajes[j], puntajes[j+1] = puntajes[j+1], puntajes[j]
    return puntajes


puntajes = [78, 56, 79, 23, 90, 14, 67, 90]
print("Puntajes originales:", puntajes)
print("Puntajes ordenados:", burbuja_puntajes(puntajes))
