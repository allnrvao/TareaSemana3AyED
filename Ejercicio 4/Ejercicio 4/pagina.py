import model.inventario as inventario_module
import model.producto as producto_module

def limpiar_consola():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar_entrada():
    input("Presione Enter para continuar...")

def main():

    inventario = inventario_module.Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar Producto")
        print("2. Buscar Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            producto = producto_module.Producto(codigo, nombre, precio, stock)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            codigo = input("Ingrese el código del producto a buscar: ")
            producto = inventario.buscar_producto(codigo)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            codigo = input("Ingrese el código del producto a actualizar: ")
            nombre = input("Ingrese el nuevo nombre (dejar vacío para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar vacío para no cambiar): ")
            stock = input("Ingrese el nuevo stock (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(codigo, nombre or None, float(precio) if precio else None, int(stock) if stock else None)

        elif opcion == "4":
            codigo = input("Ingrese el código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            break

        else:
            print("Opción inválida. Intente nuevamente.")

        pausar_entrada()

if __name__ == "__main__":
    main()
