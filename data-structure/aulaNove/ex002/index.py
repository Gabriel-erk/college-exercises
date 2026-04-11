class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def inserir_fim(head, valor):
    novoNo = Node(valor)
    if head == None:
        head = novoNo
    while head.next is not None:
        head = head.next
    last = head
    last.next = novoNo

def listar_todos(head):
    while head is not None:
        print(head.data)
        head = head.next

n1 = Node(5)
n2 = Node(10)
n3 = Node(15)

n1.next = n2
n2.next = n3

head = n1

inserir_fim(head, 10)
inserir_fim(head, 20)
inserir_fim(head, 30)
listar_todos(head)

