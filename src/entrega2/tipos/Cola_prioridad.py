
from typing import TypeVar, Generic, List, Tuple

E = TypeVar('E')
P = TypeVar('P')

class Cola_de_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[Tuple[P, E]] = []
        self._priorities: List[Tuple[P, E]] = []
    
    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    def elements(self) -> List[E]:
        return [element for _, element in self._elements]
    
    def add(self, e: E, priority: P):
        index = self.__index_order__(priority)
        self._elements.insert(index, (priority, e))
       
    def add_all(self, Is: List[Tuple[E, P]]):
        for e, priority in Is:
            self.add(e, priority)

    def remove(self) -> E:
        if self.is_empty():
            raise IndexError("remove from empty priority queue")
        return self._elements.pop(0)[1]  # remueve y devuelve el elemento con la mayor prioridad 

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        return removed_elements

    def __index_order__(self, priority: P) -> int:
        for index, (p, _) in enumerate(self._elements):
            if priority < p:
                return index
        return len(self._elements)

    def decrese_priority(self, e: E, nueva_priority: P)->None:
        for index, (nueva_priority, e) in enumerate(self._elements):
            if e == e:
                del self._elements[index]
                self.add(e, nueva_priority)
                return
        raise ValueError("Element not found in the priority queue")
