# Ordenación de ventas diarias: Se registraron ventas diarias de una tienda. Ordénalas en orden
# ascendente con inserción.


def insercion_ventas(ventas):
    for i in range(1, len(ventas)):
        clave = ventas[i]
        j = i - 1
        while j >= 0 and ventas[j] > clave:
            ventas[j + 1] = ventas[j]
            j -= 1
        ventas[j + 1] = clave
    return ventas


ventas = [250000, 4000000, 380000, 545000, 1300000, 890000, 7654400]
print("Ventas diarias originales:", ventas)
print("Ventas diarias ordenadas en orden ascendente:", insercion_ventas(ventas))


