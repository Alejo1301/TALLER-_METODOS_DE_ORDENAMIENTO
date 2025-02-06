# Ordenación de nombres por orden alfabético inverso: Usa el método burbuja

def burbuja_nombres_inverso(nombres):
    n = len(nombres)
    for i in range(n-1):
        for j in range(n-i-1):
            if nombres[j] < nombres[j+1]:
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
    return nombres


nombres = ["MARIA", "PEDRO", "SARA", "ELENA", "WENDY", "KATHERINA", "YULIANA"]

print("Nombres :")
print(nombres)

print("Nombres ordenados en orden alfabético inverso:")
print(burbuja_nombres_inverso(nombres))

