
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar, Generic, List

E = TypeVar('E')

class Pila(Agregado_lineal[E], Generic[E]):
    def __init__(self):
        super().__init__()
        self._elements: List[E] = []

    @staticmethod
    def of() -> 'Pila[E]':
        """Método de factoría que crea e inicializa una nueva instancia de la clase."""
        return Pila()
    
    def add(self, e: E) -> None:
        """Añade un elemento e a la parte superior de la pila."""
        self._elements.insert(0, e)

        
    def __str__(self) -> str:
        return f"{self._elements}"
