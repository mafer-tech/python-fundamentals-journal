# Pedirle datos al usuario
nombre = input("¿Cómo te llamas? ")
print("Mucho gusto ", nombre)

# Convertir el texto ingresado a entero
edad = int(input("¿Cuántos años tienes? "))
print(edad)

# EJERCICIO 2:
product_name = input("Ingrese el nombre del producto ")
price = float(input("Ingrese el precio del producto "))
descuento = price * 0.10
final_price = price - descuento

print("Tu producto es: ", product_name, "y el precio antes de descuento es: ", price, "el precio total con el -10% de descuento es: ", final_price)
