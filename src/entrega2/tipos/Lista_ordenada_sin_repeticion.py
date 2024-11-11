from entrega2.tipos.Agregado_lineal import Agregado_lineal,E,R
from typing import Callable,Generic

class Lista_ordenada_sin_repeticiones(Agregado_lineal,Generic[E,R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

        
    @staticmethod
    def of(order: Callable[[E],R])-> 'Lista_ordenada_sin_repeticiones[E,R]':
        return Lista_ordenada_sin_repeticiones(order)
    
    def __index_order(self,e:E)->int:
        for i,existe in enumerate(self._elements):
            if self._order(e) < self._order(existe):
                return i
        return len(self._elements)

    def add(self,e:E)->None:
        if e not in self._elements:
            index = self.__index_order(e)
            self._elements.insert(index,e)
            
    def __str__(self) -> str:
        return f"Lista_ordenada_sin_repeticiones([{', '.join(map(str, self._elements))}])"
