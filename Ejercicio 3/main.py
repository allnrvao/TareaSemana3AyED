# Ejercicio 3: Paquete de algoritmos de búsqueda

import controllers.search_dao as dao
import models.lineal_search as linear
import models.binary_search as binary
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_lista():
    entrada = input("Ingrese una lista de números separados por espacios o comas: ")
    return list(map(int, entrada.replace(',', ' ').split()))

def mostrar_resultado(nombre, resultado):
    if resultado != -1:
        print(f"{nombre} -> Número encontrado en la posición: {resultado}")
    else:
        print(f"{nombre} -> Número NO encontrado.")

def main():
    limpiar_pantalla()

    search_dao = dao.SearchDAO()
    
    print("=" * 40)
    print("     Sistema de Algoritmos de Búsqueda     ")
    print("=" * 40)

    data = pedir_lista()
    target = int(input("Ingrese el número a buscar: "))
    sorted_data = sorted(data)

    print(f"\nLista ingresada: {data}")
    print(f"Número objetivo: {target}")
    print("-" * 40)

    # Búsqueda lineal
    resultado_lineal = search_dao.search('linear', data, target)
    mostrar_resultado("Búsqueda Lineal", resultado_lineal)

    # Búsqueda binaria
    resultado_binaria = search_dao.search('binary', sorted_data, target)
    mostrar_resultado("Búsqueda Binaria (Lista Ordenada)", resultado_binaria)

    print("-" * 40)
    print("Fin del programa.")

if __name__ == "__main__":
    main()
