class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def remover_duplicados(head):
    current = head

    while current:
        atual2 = current
        while atual2.next:
            if atual2.next.data == current.data:
                atual2.next = atual2.next.next  
            else:
                atual2 = atual2.next
        current = current.next

    return head

n1 = Node(1)
n2 = Node(2)
n3 = Node(1)
n4 = Node(3)
n5 = Node(2)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1

head = remover_duplicados(head)

atual = head
while atual:
    print(atual.data)
    atual = atual.next