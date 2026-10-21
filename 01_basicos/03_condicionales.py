# Toma de decisiones (if / else)
edad = int(input("¿Cuál es tu edad?: "))
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

# EJERCICIO 3:
producto = input("ingrese el nombre del producto ")
precio = float(input("ingrese el precio "))
if precio > 50:
    descuento1 = precio * 0.20
    precio_desc = precio - descuento1
    print("obtuvo un descuento por una compra grande, su total es: ", precio_desc)
else:
    print("no aplica descuento por ser una compra menor a 50, su precio es: ", precio)
