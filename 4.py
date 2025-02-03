# Orden de llegada de corredores: Dado un listado de tiempos de llegada en una carrera,
# ordénalos de menor a mayor usando burbuja

def burbuja_tiempos(tiempos):
    n = len(tiempos)
    for i in range(n-1):
        for j in range(n-i-1):
            if tiempos[j] > tiempos[j+1]:
                tiempos[j], tiempos[j+1] = tiempos[j+1], tiempos[j]
    return tiempos


tiempos = [2.65, 1,79, 10,6, 3.78, 3.0, 2.50, 1.67]
print("Tiempos de llegada originales:", tiempos)
print("Tiempos de llegada ordenados de menor a mayor:", burbuja_tiempos(tiempos))