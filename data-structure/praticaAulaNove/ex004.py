class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def contar_ocorrencias(head, valor_alvo):
    contador_ocorrencias = 0
    while head is not None:
        if head.data == valor_alvo:
            contador_ocorrencias += 1
        head = head.next
    
    return f"Valor - {valor_alvo} aparece: {contador_ocorrencias}x na lista."

n1 = Node(3)
n2 = Node(6)
n3 = Node(3)
n4 = Node(9)
n5 = Node(3)
n6 = Node(12)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

head = n1

print(contar_ocorrencias(head, 3))
print(contar_ocorrencias(head, 8))