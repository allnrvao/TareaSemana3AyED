import model.producto as producto_module
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print("Ya existe un producto con ese código.")
        else:
            self.productos[producto.codigo] = producto
            print("Producto agregado con éxito.")

    def buscar_producto(self, codigo):
        return self.productos.get(codigo, None)

    def actualizar_producto(self, codigo, nombre=None, precio=None, stock=None):
        producto = self.buscar_producto(codigo)
        if producto:
            if nombre is not None:
                producto.nombre = nombre
            if precio is not None:
                producto.precio = precio
            if stock is not None:
                producto.stock = stock
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)
