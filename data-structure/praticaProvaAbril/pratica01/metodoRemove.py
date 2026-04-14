class Node:
    def __init__(self, data):
        self.data = data
        self. next = None

def remover(head, valor_alvo):
    previous = None
    found = False
    
    while not found:
        if head.data == valor_alvo:
            found = True
            break
        previous = head        
        head = head.next
    
    if not found:
        return "Valor não encontrado."
    
    previous.next = head.next
    return "Valor removido."

def show(head):
    while head is not None:
        print(head.data)
        head = head.next

n1 = Node(10)
n2 = Node(5)
n3 = Node(20)
n4 = Node(15)
n5 = Node(19)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1

show(head)
print(remover(head, 20))
show(head)

