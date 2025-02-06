# Ranking de puntuaciones: Un juego guarda las puntuaciones de jugadores. Ordena las
# puntuaciones en orden descendente usando inserción


def insercion_puntuaciones(puntuaciones):
    for i in range(1, len(puntuaciones)):
        clave = puntuaciones[i]
        j = i - 1
        while j >= 0 and puntuaciones[j] < clave:
            puntuaciones[j + 1] = puntuaciones[j]
            j -= 1
        puntuaciones[j + 1] = clave
    return puntuaciones


puntuaciones = [1700, 500, 150, 8, 1600, 1000, 1770]
print("Puntuaciones originales:", puntuaciones)
print("Puntuaciones ordenadas en orden descendente:", insercion_puntuaciones(puntuaciones))