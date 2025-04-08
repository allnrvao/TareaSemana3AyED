#metodo de ordenamiento
def bubble_sort(lista_estudiantes):
    n = len(lista_estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_estudiantes[j].getPromedio() > lista_estudiantes[j + 1].getPromedio():
                lista_estudiantes[j], lista_estudiantes[j + 1] = lista_estudiantes[j + 1], lista_estudiantes[j]
    return lista_estudiantes
    
    