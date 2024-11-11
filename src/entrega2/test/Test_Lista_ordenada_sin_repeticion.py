from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticiones
print("TEST LISTA ORDENADA SIN REPETICIONES")

def test_lista_ordenada_sin_repeticion():
    # Creación de una lista con criterio de orden
    order_function = lambda x: -x
    lista = Lista_ordenada_sin_repeticiones(order_function)
    print("###############################################\n")

    lista.add(23)
    lista.add(47)
    lista.add(47)
    lista.add(1)
    lista.add(2)
    lista.add(-3)
    lista.add(4)
    lista.add(5)
    print("Creacion de una Lista con Criterio de orden lambdax: -x\n")
    print("Se añade en este orden: 23, 47, 47, 1, 2, -3, 4, 5\n")
    print(f"Resultado de la lista: {lista}\n")
    
    print("###############################################\n")
    
    removed_element = lista.remove()
    print(f"El elemento eliminado al utlizar remove () : {removed_element}\n")
    
    print("###############################################\n")
      
    lista.add(47)
    removed_elements = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}\n")
    
    print("###############################################\n")
    
    lista.add(23)
    lista.add(47)
    lista.add(47)
    lista.add(1)
    lista.add(2)
    lista.add(-3)
    lista.add(4)
    lista.add(5)
    lista.add(0) 
    print(f"Lista después de añadirle el 0: {lista}\n")
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}\n")
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}\n")

if __name__ == '__main__':
    test_lista_ordenada_sin_repeticion()