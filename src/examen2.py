

# Examen 2
from entrega2.tipos.Agregado_lineal import Agregado_lineal, E

class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        self.capacidad = capacidad
        self.elementos = []

    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError('La cola está llena')
        self.elementos.append(e)
      
    def remove(self) -> E:
        if not self.elementos:
            raise IndexError('La cola está vacía')
        return self.elementos.pop(0)
        
    @classmethod
    def of(cls, capacidad: int) -> "ColaConLimite":
        return cls(capacidad)

    def is_full(self) -> bool:
        return len(self.elementos) >= self.capacidad

def test_cola_con_limite():
    cola = ColaConLimite.of(3)
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")

    try:
        cola.add("Tarea 4")
    except OverflowError as e:
        print(e)
    print(cola.remove())

def test_cola_con_limite2():
    cola = ColaConLimite.of(5)
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")
    cola.add("Tarea 4")
    

    try:
        cola.add("Tarea 6")
    except OverflowError as e:
        print(e)
    print(cola.remove())


#Problema 2 
# Modificque el codigo en directamente en Agredado Lineal:
 
#Aqui Hare las pruebas de las funciones que he agregado:

def test_contains():
    agregado = Agregado_lineal[int]()
    agregado.add_all([1, 2, 3, 4, 5])

    print("Prueba de contains:")
    print(f"Contiene 3: {agregado.contains(3)}")  # Debe ser True
    print(f"Contiene 6: {agregado.contains(6)}")  # Debe ser False

def test_find():
    agregado = Agregado_lineal[int]()
    agregado.add_all([1, 2, 3, 4, 5])

    print("\nPrueba de find:")
    print(f"Encontrar 4: {agregado.find(lambda x: x == 4)}")  # Debe ser 4
    print(f"Encontrar 10: {agregado.find(lambda x: x == 10)}")  # Debe ser None

def test_filter():
    agregado = Agregado_lineal[int]()
    agregado.add_all([1, 2, 3, 4, 5])

    print("\nPrueba de filter:")
    print(f"Filtrar números pares: {agregado.filter(lambda x: x % 2 == 0)}")  # Debe ser [2, 4]


if __name__ == '__main__':
    print("Cuando la cola esta llena:\n")
    test_cola_con_limite()
    print("################################################################################\n")
    print("Cuando la cola no esta llena se puede agregar otro elemento hasta el limite:\n")
    test_cola_con_limite2()
    print("################################################################################\n")
    test_contains()
    test_find()
    test_filter()
    