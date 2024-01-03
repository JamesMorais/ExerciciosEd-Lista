class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def insertAtFirst(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def removeFromLast(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


def main():
    list = ListaEncadeada()

    # Inserindo alguns elementos na primeira posição
    list.insertAtFirst(3)
    list.insertAtFirst(7)
    list.insertAtFirst(1)

    # Imprimindo a lista
    list.printList()

    # Removendo da última posição
    list.removeFromLast()

    # Imprimindo a lista após a remoção
    list.printList()


if __name__ == "__main__":
    main()
