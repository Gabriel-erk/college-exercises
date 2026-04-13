class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def show(head):
    while head is not None:
        print(f"Cod: {head.data}")
        head = head.next

def inserir_fim(head, valor_a_adicionar):
    novoNo = Node(valor_a_adicionar)
    if head == None:
        head = novoNo
        return head
    
    while head.next is not None:
        head = head.next
    
    ultimo = head
    ultimo.next = novoNo

def buscar(head, valor_a_procurar):
    while head is not None:
        if head.data == valor_a_procurar:
            return True
        head = head.next
    return False

def contar_ocorrencias(head, valor_a_contar):
    contador_ocorrencias = 0
    while head is not None:
        if head.data == valor_a_contar:
            contador_ocorrencias += 1
        head = head.next
    return f"Código: {valor_a_contar} aparece {contador_ocorrencias}x na lista."

n1 = Node(101)
n2 = Node(205)
n3 = Node(101)
n4 = Node(330)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1

show(head)
print("-------")
inserir_fim(head, 450)
show(head)
print("-------")
if buscar(head, 205):
    print("O código: 205 está na lista.")
else:
    print("O código 205 não está na lista.")
print("-------")
print(contar_ocorrencias(head, 101))
print("-------")
show(head)