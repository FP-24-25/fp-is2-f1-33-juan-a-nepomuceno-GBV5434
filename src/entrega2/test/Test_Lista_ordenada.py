
from entrega2.tipos.Lista_ordenada import Lista_ordenada
print("TEST LISTA ORDENADA")

def test_lista_ordenada():
    # Creación de una lista con criterio de orden
    order_function = lambda x: x
    lista = Lista_ordenada(order_function)
    print("###############################################\n")

    # Se añade en este orden: 3, 1, 2
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print("Creacion de una lista con criterio de orden lambda x: x\n")
    print("Se añade en este orden: 3, 1, 2\n")
    print(f"Resultado de la lista: {lista}\n")    # nos devuelve la lista ordenada
    
    print("###############################################\n")
    
    
    removed_element = lista.remove()
    print(f"El elemento eliminado al utlizar remove () : {removed_element}\n")
    
    print("###############################################\n")
      
    lista.add(1)
    removed_elements = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}\n")
    
    print("###############################################\n")
    
    lista.add(3)
    lista.add(2)
    lista.add(1)
    lista.add(0) 
    print(f"Lista después de añadirle el 0: {lista}\n")
    lista.add(10)
    print(f"Lista después de añadirle el 10: {lista}\n")
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}\n")

if __name__ == "__main__":
    test_lista_ordenada()
    
