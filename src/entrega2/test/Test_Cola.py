from entrega2.tipos.Cola import Cola

print("TEST COLA")
print("###############################################\n")
def test_cola():
    cola = Cola.of()
    cola.add(23)
    cola.add(47)
    cola.add(1)
    cola.add(2)
    cola.add(-3)
    cola.add(4)
    cola.add(5)
    print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5\n")
    print(f'Resultado de la cola:{cola}\n')
    print("###############################################\n")
    cola_removed = cola.remove_all()
    print(f'Elementos eliminados utilizando remove_all: {cola_removed}\n')
    
if __name__ == '__main__':
    test_cola()