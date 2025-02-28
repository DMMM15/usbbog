#!/usr/bin/env python3

"""
Título de práctica: taller tienda1

Se desarrolla un programa que maneje el inventario de una tienda con 3 productos que tengan los atributos de nombre, precio unitario y cantidad
y donde al final se muestren los datos recopilados en una tabla.

Autor: David Mateo Moyano Mahecha <mateomoyano1517@gmail.com>
Fecha: 2025-02-01
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí

    # Saludo
    class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio  # Precio en pesos COP
        self.cantidad = cantidad  # Cantidad en unidades

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio} COP, Cantidad: {self.cantidad} unidades"

# Lista para almacenar los productos
productos = []

# Solicitar información de 3 productos
for i in range(3):
    print(f"Ingrese los datos del producto {i + 1}:")
    nombre = input("Nombre: ")
    precio = float(input("Precio unitario (COP): "))
    cantidad = int(input("Cantidad (unidades): "))
    
    producto = Producto(nombre, precio, cantidad)
    productos.append(producto)
    print()

# Mostrar información de los productos ingresados
print("Productos ingresados:")
for producto in productos:
    print(producto.mostrar_info())
    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
