from typing import List
from abc import ABC, abstractmethod

class EstrategiaOrdenamiento(ABC):
    @abstractmethod
    def ordenar(self, datos: List[int]) -> List[int]:
        pass

class OrdenamientoBurbuja(EstrategiaOrdenamiento):
    def ordenar(self, datos: List[int]) -> List[int]:
        print("Usando ordenamiento burbuja")
        n = len(datos)
        for i in range(n):
            for j in range(0, n-i-1):
                if datos[j] > datos[j+1]:
                    datos[j], datos[j+1] = datos[j+1], datos[j]
        return datos

class OrdenamientoRapido(EstrategiaOrdenamiento):
    def ordenar(self, datos: List[int]) -> List[int]:
        print("Usando ordenamiento rápido")
        if len(datos) <= 1:
            return datos
        pivote = datos[0]
        menores = [x for x in datos[1:] if x < pivote]
        mayores = [x for x in datos[1:] if x >= pivote]
        return self.ordenar(menores) + [pivote] + self.ordenar(mayores)

class ListaNumeros:
    def __init__(self, estrategia: EstrategiaOrdenamiento):
        self._estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaOrdenamiento):
        self._estrategia = estrategia

    def ordenar(self, datos: List[int]) -> List[int]:
        return self._estrategia.ordenar(datos)

datos = [10, 3, 5, 2, 8,25,7,5,15]

lista = ListaNumeros(OrdenamientoBurbuja())
print("Resultado:", lista.ordenar(datos.copy()))

lista.set_estrategia(OrdenamientoRapido())
print("Resultado:", lista.ordenar(datos.copy()))