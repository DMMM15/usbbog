import unittest

class Producto:
    """Clase que representa un producto en el inventario de la tienda."""
    
    def __init__(self, nombre: str, precio: float, cantidad: int):
        """Inicializa un producto con nombre, precio unitario y cantidad."""
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_info(self):
        """Muestra la información del producto con el formato adecuado."""
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f} COP, Cantidad: {self.cantidad} unidades"


def main():
  
    productos = []
    
    for i in range(3):
        print(f"Ingrese los datos del producto {i + 1}:")
        nombre = input("Nombre: ")
        precio = float(input("Precio unitario (COP): "))
        cantidad = int(input("Cantidad en unidades: "))
        
        producto = Producto(nombre, precio, cantidad)
        productos.append(producto)
        print()
    
    print("\nInventario de la tienda:")
    for producto in productos:
        print(producto.mostrar_info())


class TestProducto(unittest.TestCase):
    """Clase de pruebas unitarias para la clase Producto."""
    
    def test_creacion_producto(self):
        """Prueba la creación de un producto."""
        producto = Producto("Manzana", 2.500, 10)
        self.assertEqual(producto.nombre, "Manzana")
        self.assertEqual(producto.precio, 2.500)
        self.assertEqual(producto.cantidad, 10)
    
    def test_mostrar_info(self):
        """Prueba el método mostrar_info."""
        producto = Producto("Pan", 1500.00, 5)
        self.assertEqual(producto.mostrar_info(), "Producto: Pan, Precio: $1500.00 COP, Cantidad: 5 unidades")

        if __name__ == "__main__":
    main()