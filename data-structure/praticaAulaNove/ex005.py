class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def show(head):
    while head is not None:
        print(head.data)
        head = head.next

def inserir_fim(head, data):
    novoNo = Node(data)
    if head == None:
        head = novoNo
        return head
    
    while head.next is not None:
        head = head.next
    
    last = head
    last.next = novoNo

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
    print(f"Valor: {valor_a_contar} aparece {contador_ocorrencias}x na lista.")

n1 = Node(5)
n2 = Node(10)
n3 = Node(5)
n4 = Node(20)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1

print("LETRA a)")
show(head)
print("LETRA b)")
inserir_fim(head, 30)
show(head)
print("LETRA c)")
valor_a_procurar = int(input("Digite o valor a procurar:"))
if buscar(head, valor_a_procurar):
    print(f"Valor: {valor_a_procurar} está na lista.")
else:
    print(f"Valor: {valor_a_procurar} não está na lista.")
print("LETRA d)")
contar_ocorrencias(head, 5)
print("LETRA e)")
show(head)