# Bucles (while)
contador = 1

while contador <= 3:
    print("Numero: ", contador)
    contador = contador + 1
print("Fin del conteo")

# EJERCICIO 4:
opcion = ""
if opcion == "salir":
    print("Gracias por tu compra")
else:
    while opcion != "salir":
        producto = input("ingrese nombre del producto ")
        print("hola, su producto es: ", producto)
        opcion = input("si desea salir escriba salir: ")
