class Estudiante:
    def __init__(self, nombre, c1, c2, c3, promedio, estado):
        self.__nombre = nombre
        self.__calificacion1 = c1
        self.__calificacion2 = c2
        self.__calificacion3 = c3
        self.__promedio = promedio 
        self.__estado = estado

    def getNombre(self):
        return self.__nombre  

    def getPromedio(self):
        return self.__promedio
    
    def getEstado(self):
        return self.__estado
    