class Cliente:
    def __init__(self, id, nombre, contacto, descuento):
        self.id = id
        self.nombre = nombre
        self.contacto = contacto
        self.descuento = descuento

    def calcular_total(self, pedidos):
        total = sum(pedido.precio for pedido in pedidos)
        return total * (1 - self.descuento / 100)

class Pedido:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio
