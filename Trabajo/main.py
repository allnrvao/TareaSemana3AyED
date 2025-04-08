from producto import Producto
class Main:
    def __init__(self):
        pass
    def main(self):
        product = []
        #bienvenida al usuario
        print("BIENVENIDO AL PROGRAMA DE VENTAS")
        print("Ingrese la cantidad de productos a agregar al inventario: ", end= '')
        n = int(input())
        #un for para agregar la cantidad de productos que el usuario requiera
        for i in range(n):
            
            #se le piden los datos al usuario
            print(f"ingrese el nombre del producto {i + 1}: ", end= '')
            nombreProducto = input()
            print(f"ingrese el codigo del producto {i + 1}: ", end= '')
            codigoProducto = int(input())
            print(f"ingrese la cantidad del producto {i + 1}: ", end= '')
            cantidadProducto = int(input())
            print(f"ingrese el precio del producto {i + 1}: ", end= '')
            precioProducto = float(input())
            
            #Asignar los valores a cada variable en la clase
            prod = Producto(nombreProducto, precioProducto, cantidadProducto, codigoProducto)
            
        #almacenar los datos del producto en la lista de producto
            product.append(prod)
        #mostrar los productos almacenados
        print("Los productos agregados son:")
        for emp in product:
            print(f"Nombre: {emp.getNombre()}, Código: {emp.getCodigo()}, Cantidad: {emp.getCantidad()}, Precio: $ {emp.getPrecio()}")