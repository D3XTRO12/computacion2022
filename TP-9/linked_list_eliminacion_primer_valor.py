class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.Head = None

    def imprimir_lista(self):
        current = self.Head
        while current is not None:
            print(current.data, end = " ")
            current = current.next
        print("")

    def insertar_en_posicion(self, elemento, posicion):
        counter = 1
        current = self.Head
        while counter < posicion - 1 and current is not None:
            counter += 1
            current = current.next
        if posicion == 1:
            newNode = Node(elemento)
            newNode.next = current
            self.Head = newNode
        else:
            newNode = Node(elemento)
            newNode.next = current.next
            current.next = newNode

    def eliminar_desde_inicio(self):
        if self.Head is None:
            print("The linked list empty. Cannot delete an element.")
            return
        else:
            node = self.Head
            self.Head = self.Head.next
            del node


myLinkedList = LinkedList()
myLinkedList.insertar_en_posicion(10, 1)
myLinkedList.insertar_en_posicion(20, 2)
myLinkedList.insertar_en_posicion(30, 3)
myLinkedList.insertar_en_posicion(40, 2)
print("Los elementos de la lista enlazada son:")
myLinkedList.imprimir_lista()
myLinkedList.eliminar_desde_inicio()
print("Los elementos de la lista enlazada son:")
myLinkedList.imprimir_lista()
myLinkedList.eliminar_desde_inicio()
print("Los elementos de la lista enlazada son:")
myLinkedList.imprimir_lista()