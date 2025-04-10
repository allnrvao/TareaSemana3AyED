class Factura:
    def __init__(self, nombre_producto, cantidad, precio_unitario, impuesto):
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.impuesto = impuesto
    
    def calcular_total(self):
        if self.validaciones():
            raise ValueError("Datos inválidos.")
        else:
            return self.precio_unitario * self.cantidad * (1 - self.impuesto)
    
    def generar_reporte(self):
        return (
            f"Producto: {self.nombre_producto}\n"
            f"Cantidad: {self.cantidad}\n"
            f"Precio unitario: ${self.precio_unitario:.2f}\n"
            f"Impuesto aplicado: {self.impuesto * 100:.2f}%\n"
            f"Total: ${self.calcular_total():.2f}"
        )

    def validaciones(self):
        if not isinstance(self.nombre_producto, str):
            return "Error: El nombre del producto debe ser una cadena de texto."
        if not isinstance(self.cantidad, int):
            return "Error: La cantidad debe ser un número entero."
        if not isinstance(self.precio_unitario, float):
            return "Error: El precio debe ser un número decimal."
        if not isinstance(self.impuesto, float):
            return "Error: El impuesto debe ser un número decimal."
        return None
