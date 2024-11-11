from entrega2.tipos.Pila import Pila
print("TEST PILA")
print("###############################################\n")
def Test_Pila():
    pila = Pila.of()
    print("Hemos agregado en orden 1,4,2,5,9,28 y vemos que cada nuevo elemento se va agregando a la parte superior de la pila\n")
    pila.add(1)
    pila.add(4)
    pila.add(2)
    pila.add(5)
    pila.add(9)
    pila.add(28)
    print(pila)



if __name__ == '__main__':
    Test_Pila()