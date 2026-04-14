class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_last(head, valor_a_adicionar):
    novo_no = Node(valor_a_adicionar)
    if head == None:
        head = novo_no
        return head
    
    while head.next is not None:
        head = head.next
    
    ultimo = head
    ultimo.next = novo_no
    
    return head

def show(head):
    while head is not None:
        print(head.data)
        head = head.next

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

print("Antes de adicionar por último:")
show(head)
print("Após adicionar por último:")
add_last(head, 60)
show(head)