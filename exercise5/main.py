import exercise5.models.cliente as m
import controllers.client_controllers as cc  # Puedes eliminar esta línea si no usas los controladores

def obtener_entero_valido(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"Ingrese un número entre {minimo} y {maximo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")

def obtener_decimal_valido(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"Ingrese un número entre {minimo} y {maximo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Debe ser un número decimal.")

def obtener_cadena_no_vacia(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede estar vacío.")

def crear_cliente(tipo_cliente):
    print(f"\nCreando cliente {tipo_cliente.upper()}:")
    cliente_id = obtener_entero_valido("ID del cliente: ", minimo=1)
    nombre = obtener_cadena_no_vacia("Nombre del cliente: ")
    telefono = obtener_cadena_no_vacia("Teléfono del cliente: ")

    if tipo_cliente == "VIP":
        descuento = obtener_entero_valido("Descuento (%) del cliente VIP: ", minimo=0, maximo=100)
    else:
        descuento = 0

    return m.Cliente(cliente_id, nombre, telefono, descuento)

def crear_pedido(tipo_cliente):
    print(f"\nAgregando pedido para cliente {tipo_cliente}:")
    comida = obtener_decimal_valido("Precio de la comida: ", minimo=0)
    bebida = obtener_decimal_valido("Precio de la bebida: ", minimo=0)
    return [
        m.Pedido("comida", comida),
        m.Pedido("bebida", bebida)
    ]

def main():
    cliente_regular = None
    cliente_vip = None
    pedido_regular = []
    pedido_vip = []

    while True:
        print("\nMenú Principal:")
        print("1. Crear Cliente Regular")
        print("2. Crear Cliente VIP")
        print("3. Agregar Pedido a Cliente Regular")
        print("4. Agregar Pedido a Cliente VIP")
        print("5. Calcular Totales")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            cliente_regular = crear_cliente("regular")
        elif opcion == "2":
            cliente_vip = crear_cliente("VIP")
        elif opcion == "3":
            if cliente_regular:
                pedido_regular = crear_pedido("regular")
            else:
                print("Debe crear un cliente regular primero.")
        elif opcion == "4":
            if cliente_vip:
                pedido_vip = crear_pedido("VIP")
            else:
                print("Debe crear un cliente VIP primero.")
        elif opcion == "5":
            print("\nTotales:")
            if cliente_regular:
                total = cliente_regular.calcular_total(pedido_regular)
                print(f"Total Cliente Regular: ${total:.2f}")
            else:
                print("Cliente regular no registrado.")

            if cliente_vip:
                total = cliente_vip.calcular_total(pedido_vip)
                print(f"Total Cliente VIP (con descuento): ${total:.2f}")
            else:
                print("Cliente VIP no registrado.")
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
