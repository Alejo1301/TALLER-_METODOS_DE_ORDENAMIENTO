# Ordenación de precios de productos: Un sistema de inventario tiene precios desordenados.
# Ordénalos ascendentemente con burbuja


def burbuja_precios(precios):
    n = len(precios)
    for i in range(n-1):
        for j in range(n-i-1):
            if precios[j] > precios[j+1]:
                precios[j], precios[j+1] = precios[j+1], precios[j]
    return precios


precios = [50000, 3000, 5000, 245, 2000, 5600, 1500]
print("Precios originales:", precios)
print("Precios ordenados ascendentemente:", burbuja_precios(precios))



