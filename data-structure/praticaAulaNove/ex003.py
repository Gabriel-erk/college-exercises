class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def buscar(head, valor_procurado):
    while head is not None:
        if head.data == valor_procurado:
            return True
        head = head.next
    return False

n1 = Node(4)
n2 = Node(9)
n3 = Node(12)
n4 = Node(18)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1

valor_procurado = int(input("Digite o valor procurado: "))

if buscar(head,valor_procurado):
    print(f"O valor: {valor_procurado} está na lista.")
else:
    print(f"O valor: {valor_procurado} não está na lista.")