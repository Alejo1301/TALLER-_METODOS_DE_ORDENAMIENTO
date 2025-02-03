# Temperaturas diarias: Un sensor registra las temperaturas de una semana. Ordena los valores
# de mayor a menor utilizando burbuja.

def burbuja_temperaturas(temperaturas):
    n = len(temperaturas)
    for i in range(n-1):
        for j in range(n-i-1):
            if temperaturas[j] < temperaturas[j+1]:
                temperaturas[j], temperaturas[j+1] = temperaturas[j+1], temperaturas[j]
    return temperaturas


temperaturas = [33, 15, 28.3, 26, 22, -1, 0]
print("Temperaturas originales:", temperaturas)
print("Temperaturas ordenadas de mayor a menor:", burbuja_temperaturas(temperaturas))
