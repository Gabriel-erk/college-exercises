class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def inserir_fim(head, data):
    newN = Node(data)
    # se o head já estiver vazio, foi passada uma lista sem valores, entaõ o primeiro valor dela vai ser o novo valor que recebemos (é definido como o primeiro da lista pois atribuo o valor do head daquela lista como um objeto instanciado a partir da classe node passado o valor que recebemos de parâmetro)
    if head == None:
        head = newN
        return head  # assim o novo nó virao novo head
    
    while head.next is not None:
        head = head.next
    
    last = head
    last.next = newN
    return head

def mostrar_lista(head):
    while head is not None:
        print(head.data)
        head = head.next

n1 = Node(4)
n2 = Node(8)
n3 = Node(14)

n1.next = n2
n2.next = n3

head = n1

inserir_fim(head, 10)
mostrar_lista(head)
inserir_fim(head, 20)
mostrar_lista(head)
inserir_fim(head, 30)
mostrar_lista(head)