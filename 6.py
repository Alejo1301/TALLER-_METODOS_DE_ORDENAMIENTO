# Ordenación de edades: Un grupo de personas tiene diferentes edades. Utiliza inserción para
# ordenarlas de menor a mayor.

def insercion_edades(edades):
    for i in range(1, len(edades)):
        clave = edades[i]
        j = i - 1
        while j >= 0 and edades[j] > clave:
            edades[j + 1] = edades[j]
            j -= 1
        edades[j + 1] = clave
    return edades


edades = [34, 9, 40, 5, 28, 7, 70]
print("Edades sin ordena:", edades)
print("Edades ordenadas de menor a mayor:", insercion_edades(edades))