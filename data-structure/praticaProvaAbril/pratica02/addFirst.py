class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def show(head):
    while head is not None:
        print(head.data)
        head = head.next

def add_first(head, data):
    novoNo = Node(data)
    novoNo.next = head
    return novoNo

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1

print("Antes de adicionar:")
show(head)

print("Após adicionar:")
head = add_first(head, 5)
show(head)