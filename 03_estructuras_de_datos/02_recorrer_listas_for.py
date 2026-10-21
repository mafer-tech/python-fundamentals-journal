# Recorrer listas elemento por elemento con (for)
carrito = ["cama", "edredon", "sabana"]

print("----TU CARRITO---")
for producto in carrito:
    print("- ", producto)

# Trabajar con listas de números y operaciones
precios = [120.0, 45.5, 80.0]
total = 0.0

for precio in precios:
    total = total + precio  # Acumulas la suma

print("el total a pagar es: ", total)

# EJERCICIO 6:
precios = [150.0, 50.0, 25.5]
total = 0
for precio in precios:
    print("Producto: ", precio)
    total = total + precio
print("Total de la compra: ", total)
