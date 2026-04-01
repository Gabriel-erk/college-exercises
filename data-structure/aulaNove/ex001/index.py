class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

def mostrar_lista(head):
    while head is not None:
        print(head.data)
        head = head.next

n1 = Node(7)
n2 = Node(14)
n3 = Node(21)
n4 = Node(28)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1
mostrar_lista(head)