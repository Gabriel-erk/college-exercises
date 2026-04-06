class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(4)
n2 = Node(9)
n3 = Node(12)
n4 = Node(18)

n1.next = n2
n2.next = n3
n3.next = n4
head = n1

def buscar(head, valorAlvo)->bool:
    while head is not None:
        if head.data == valorAlvo:
            return True
        else:
            head = head.next 
    return False

if buscar(head,12) == True:
    print(f"Valor: {12} encontrado.")
else:
    print(f"Valor: {12} não encontrado.")
    
if buscar(head,5) == True:
    print(f"Valor: {5} encontrado.")
else:
    print(f"Valor: {5} não encontrado.")           