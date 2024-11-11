from __future__ import annotations
from typing import List, TypeVar , Generic
from abc import  abstractmethod


E = TypeVar('E')
R = TypeVar('R')

class Agregado_lineal(Generic[E]):
    def __init__(self):
        self._elements: List[E]=[]
    @property 
    
    def size(self)->int:
        return len(self.List)
    
    def is_empty(self)->bool:
        return len(self.List) == 0 
    
    def elements(self)->List[E]:
        return self.List 
    
    @abstractmethod
    
    def add(self, e:E)->None:
        self.List.append(e)
        
    def add_all(self, Is:List[E])->None:
        for e in Is:
            self.add(e)
    
    def remove(self)->E:
        assert len(self._elements)>0, 'El agregado esta vacio'
        return self._elements.pop(0)   
    
    def remove_all(self) -> List[E]:
        removed_elements = self._elements[:]
        self._elements.clear()
        return removed_elements

        
    
    
        
        
        
    