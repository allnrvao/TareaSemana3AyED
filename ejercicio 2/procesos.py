class Procesos:
    def calcularPromedio(self, c1, c2, c3):
        return (c1 + c2 + c3) / 3#se saca el promedio

    def clasificarEstudiante(self, promedio):
        #se clasifica segun la nota dada en el promedio
        if promedio < 69:
            return "REPROBADO"
        elif 70 <= promedio <= 79:
            return "REGULAR"
        elif 80 <= promedio <= 89:
            return "MUY BUENO"
        elif 90 <= promedio <= 100:
            return "EXCELENTE"
        else:
            return "PROMEDIO INVÁLIDO"