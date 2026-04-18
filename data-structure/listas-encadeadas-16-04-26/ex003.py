class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def busca_desordenada(head, data):
    passos = 0
    atual = head

    while atual:
        passos += 1
        if atual.data == data:
            return True, passos
        atual = atual.next

    return False, passos


def busca_ordenada(head, data):
    passos = 0
    current = head

    while current:
        passos += 1

        if current.data == data:
            return True, passos

        if current.data > data:
            return False, passos  

        current = current.next

    return False, passos

n1 = Node(1)
n2 = Node(3)
n3 = Node(5)
n4 = Node(7)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1


print(busca_desordenada(head, 5))

print(busca_ordenada(head, 5))