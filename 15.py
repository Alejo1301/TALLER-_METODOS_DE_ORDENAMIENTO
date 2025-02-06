# Ordenación de productos por fecha de caducidad: Dado un conjunto de productos con fechas de
# caducidad, ordénalos utilizando eL metodo burbuja

def burbuja_productos(productos):
    n = len(productos)
    for i in range(n-1):
        for j in range(n-i-1):
            if productos[j]["fecha_caducidad"] > productos[j+1]["fecha_caducidad"]:
                productos[j], productos[j+1] = productos[j+1], productos[j]
    return productos


productos = [
    {"nombre": "POLLO", "fecha_caducidad": "2026-02-05"},
    {"nombre": "CARNE CERDO", "fecha_caducidad": "2025-11-07"},
    {"nombre": "MOJARRA", "fecha_caducidad": "2024-10-01"},
    {"nombre": "EMPANADAS", "fecha_caducidad": "2024-06-15"},
    {"nombre": "FRIJOLES", "fecha_caducidad": "2024-03-05"}
]

print("Productos originales:")
for producto in productos:
    print(f"Nombre: {producto['nombre']}, Fecha de caducidad: {producto['fecha_caducidad']}")

print("\nProductos ordenados por fecha de caducidad:")
for producto in burbuja_productos(productos):
    print(f"Nombre: {producto['nombre']}, Fecha de caducidad: {producto['fecha_caducidad']}")


