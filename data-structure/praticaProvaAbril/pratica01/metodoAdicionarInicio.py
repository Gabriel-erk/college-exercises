class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def adicionar_inicio(head, data):
    novoNo = Node(data)
    novoNo.next = head
    return novoNo

def show(head):
    while head is not None:
        print(head.data)
        head = head.next

n1 = Node(10)
n2 = Node(20)
n1.next = n2

head = n1

show(head)
print("------")
head = adicionar_inicio(head, 5)
show(head)