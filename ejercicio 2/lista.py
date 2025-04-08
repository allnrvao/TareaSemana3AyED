#se importan los archivos como las clases a utilizar
from estudiante import Estudiante
from procesos import Procesos
from ordenamiento import bubble_sort
#inicio del programa
class InicioListas:
    def __init__(self):
        self.procesos = Procesos()

    def iniciar(self):
        estudiantes = []
        print("BIENVENIDO AL PROGRAMA DE NOTAS")
        #se le pide al usuario digitar la cantidad de estudiantes a procesar
        print("Ingrese la cantidad de estudiantes a procesar: ")
        n = int(input())
        #segun la cantidad a trabajar se reocrre un for y se le piden los datos de cada estudiante
        for i in range(n):
            print(f"\nEstudiante {i + 1}")
            nombre = input("Nombre: ")
            c1 = float(input("Calificación corte 1: "))
            c2 = float(input("Calificación corte 2: "))
            c3 = float(input("Calificación corte 3: "))
            #se asignan los valores
            promedio = self.procesos.calcularPromedio(c1, c2, c3)
            estado = self.procesos.clasificarEstudiante(promedio)

            estudiante = Estudiante(nombre, c1, c2, c3, promedio, estado)
            estudiantes.append(estudiante)#se crea un nuevo objeto y se almacena en la lista
    #se muestran los resultados de todo el proceso 
        print("\nEstudiantes ordenados por promedio:")
        estudiantes_ordenados = bubble_sort(estudiantes)#se ordenan los estudiantes segun la nota
        for est in estudiantes_ordenados:
            print(f"{est.getNombre()} - Promedio: {est.getPromedio():.2f} - Estado: {est.getEstado()}")
