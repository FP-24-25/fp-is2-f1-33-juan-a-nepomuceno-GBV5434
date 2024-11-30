from entrega2.tipos.Agregado_lineal import Agregado_lineal, E

#Estructura de datos FIFO, First In First Out
class Cola(Agregado_lineal):
    def __init__(self):
        super().__init__()

    @staticmethod
    def of() -> 'Cola[E]':
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __str__(self) -> str:
        return f"Cola([{', '.join(map(str, self._elements))}])"
        