# Ordenación de salarios: Dado un conjunto de salarios de empleados, ordénalos utilizando el
# método burbuja

def burbuja_salarios(salarios):
    n = len(salarios)
    for i in range(n-1):
        for j in range(n-i-1):
            if salarios[j] > salarios[j+1]:
                salarios[j], salarios[j+1] = salarios[j+1], salarios[j]
    return salarios


salarios = [5000000,3300000, 1243600, 9000000, 5800000,1700000,2100000]
print("Salarios originales:", salarios)
print("Salarios ordenados:", burbuja_salarios(salarios))