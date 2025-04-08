class Producto:
    def __init__(self, nombreProducto, precioProducto, cantidadProducto, codigoProducto):
        #asignar
            self.__nombre = nombreProducto
            self.__precio = precioProducto
            self.__cantidad = cantidadProducto
            self.__codigo = codigoProducto
        
    def getNombre(self):
        return self.__nombre  

    def getPrecio(self):
        return self.__precio  
    
    def getCantidad(self):
        return self.__cantidad  
    
    def getCodigo(self):
        return self.__codigo  
        