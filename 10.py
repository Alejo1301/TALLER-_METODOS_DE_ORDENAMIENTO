# Ordenación de distancia entre ciudades: Dado un arreglo con distancias entre ciudades,
# ordénalas de menor a mayor usando inserción.


def insercion_distancias(distancias):
    for i in range(1, len(distancias)):
        clave = distancias[i]
        j = i - 1
        while j >= 0 and distancias[j] > clave:
            distancias[j + 1] = distancias[j]
            j -= 1
        distancias[j + 1] = clave
    return distancias


distancias = [500, 400, 350, 300, 180, 336, 670]
print("Distancias  en kilometros :", distancias)
print("Distancias ordenadas de menor a mayor:", insercion_distancias(distancias))



