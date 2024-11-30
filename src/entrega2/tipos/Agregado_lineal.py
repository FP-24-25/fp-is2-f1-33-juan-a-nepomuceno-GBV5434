from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Optional
from abc import abstractmethod

E = TypeVar('E')
R = TypeVar('R')

class Agregado_lineal(Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return len(self._elements) == 0

    def elements(self) -> List[E]:
        return self._elements

    @abstractmethod
    def add(self, e: E) -> None:
        self._elements.append(e)

    def add_all(self, elements: List[E]) -> None:
        for e in elements:
            self.add(e)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = self._elements[:]
        self._elements.clear()
        return removed_elements

    def contains(self, e: E) -> bool:
        return e in self._elements

    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        for element in self._elements:
            if func(element):
                return element
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [element for element in self._elements if func(element)]
