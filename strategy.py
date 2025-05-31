from typing import List  # Importa List desde typing para indicar que se usarán listas de enteros
from abc import ABC, abstractmethod  # Importa clases para definir clases abstractas e interfaces

# Interfaz Strategy
class EstrategiaOrdenamiento(ABC):  # Define una clase abstracta que servirá como interfaz
    @abstractmethod
    def ordenar(self, datos: List[int]) -> List[int]:  # Método abstracto que debe implementarse
        pass  # No se implementa aquí, se deja a las subclases concretas

# Estrategias concretas
class OrdenamientoBurbuja(EstrategiaOrdenamiento):  # Implementación concreta de la estrategia con el algoritmo burbuja
    def ordenar(self, datos: List[int]) -> List[int]:
        print("Usando ordenamiento burbuja")  # Mensaje para indicar qué algoritmo se está usando
        n = len(datos)  # Se obtiene la longitud de la lista
        for i in range(n):  # Bucle externo para controlar las pasadas
            for j in range(0, n-i-1):  # Bucle interno para comparar elementos adyacentes
                if datos[j] > datos[j+1]:  # Si el elemento actual es mayor que el siguiente
                    datos[j], datos[j+1] = datos[j+1], datos[j]  # Se intercambian los elementos
        return datos  # Se retorna la lista ordenada

class OrdenamientoRapido(EstrategiaOrdenamiento):  # Implementación concreta de la estrategia con el algoritmo quicksort
    def ordenar(self, datos: List[int]) -> List[int]:
        print("Usando ordenamiento rápido")  # Mensaje para indicar qué algoritmo se está usando
        if len(datos) <= 1:  # Caso base: listas de 1 o 0 elementos ya están ordenadas
            return datos
        pivote = datos[0]  # Se elige el primer elemento como pivote
        menores = [x for x in datos[1:] if x < pivote]  # Sublista con elementos menores al pivote
        mayores = [x for x in datos[1:] if x >= pivote]  # Sublista con elementos mayores o iguales al pivote
        return self.ordenar(menores) + [pivote] + self.ordenar(mayores)  # Se combinan listas recursivamente

# Contexto
class ListaNumeros:  # Clase que utiliza una estrategia de ordenamiento
    def __init__(self, estrategia: EstrategiaOrdenamiento):  # Constructor que recibe una estrategia
        self._estrategia = estrategia  # Se guarda la estrategia como atributo privado

    def set_estrategia(self, estrategia: EstrategiaOrdenamiento):  # Permite cambiar la estrategia en tiempo de ejecución
        self._estrategia = estrategia

    def ordenar(self, datos: List[int]) -> List[int]:  # Llama al método de ordenamiento de la estrategia actual
        return self._estrategia.ordenar(datos)

# Prueba del patrón Strategy
datos = [10, 3, 5, 2, 25, 7, 5, 15]  # Lista de datos desordenados

lista = ListaNumeros(OrdenamientoBurbuja())  # Se crea una instancia de ListaNumeros con la estrategia burbuja
print("Resultado:", lista.ordenar(datos.copy()))  # Se imprime el resultado del ordenamiento burbuja

lista.set_estrategia(OrdenamientoRapido())  # Se cambia la estrategia a ordenamiento rápido (quicksort)
print("Resultado:", lista.ordenar(datos.copy()))  # Se imprime el resultado del ordenamiento rápido