import json

# Diccionarios (dict)
producto = {
    "Nombre": "Laptop",
    "Precio": 1200.0,
    "disponible": True
}

print(producto["Nombre"])
print(producto["Precio"])

# EJERCICIO 8 (diccionario + funciones + condicionales)
mi_producto = {
    "nombre": "celular",
    "precio": 80.0
}

def mostrar_resumen(item):
    print("producto: ", item["nombre"])
    print("precio: $", item["precio"])

    if item["precio"] > 50:
        print("categoria: producto Premium")
    else:
        print("Categoria: producto estandar")

mostrar_resumen(mi_producto)

# GUARDAR DICCIONARIO EN ARCHIVO .JSON
mi_producto_json = {
    "Nombre": "Celular",
    "Precio": 80.0,
    "Disponible": True
}

with open("producto.json", "w") as archivo:
    json.dump(mi_producto_json, archivo, indent=4)

print("Archivo JSON creado con éxito")

# LEER ARCHIVO .JSON
with open("producto.json", "r") as archivo:
    datos_cargados = json.load(archivo)

print("---DATOS LEÍDOS DEL JSON---")
print("nombre: ", datos_cargados["Nombre"])
print("precio: ", datos_cargados["Precio"])
