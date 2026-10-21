# Agrupar código en funciones (def)
def saludar(nombre):
    print("hola ", nombre, " bienvenida")

saludar("mafe")
saludar("fernanda")

# EJERCICIO 7:
def evaluar_envio(total):
    if total > 100:
        print("Felicidades tu envío es gratis")
    else:
        print("El envío tiene un costo adicional de 10$")

evaluar_envio(150.0)
evaluar_envio(45.0)
