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
            print(current.data, end=" ")
            current = current.next

    def insertar_al_final(self, elemento):
        if self.Head is None:
            newNode = Node(elemento)
            self.Head = newNode
        else:
            current = self.Head
            while current.next is not None:
                current = current.next
            newNode = Node(elemento)
            current.next = newNode


myLinkedList = LinkedList()
myLinkedList.insertar_al_final(10)
myLinkedList.insertar_al_final(20)
myLinkedList.insertar_al_final(30)
print("Los elementos en esta lista son:")
myLinkedList.imprimir_lista()