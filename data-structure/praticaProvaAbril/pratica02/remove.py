class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove(head, elemento_a_remover):
    found = False
    previous = None
    
    while found == False and head != None:
        if head.data == elemento_a_remover:
            found = True
        else:
            previous = head
            head = head.next
    
    if found == False:
        return "Elemento não encontrado."
    # se chegou aqui significa que o found == True, logo, o anterior aponta pro proximo do elemento que quero remover == head.next(pois o valor ATUAL do head, é oq eu quero remover, logo, tenho que fazer a ponte entre o anterior do que eu quero remover e proximo do que quero remover, para que o valor que quero remover seja cortado da lista e nunca seja lido)
    previous.next = head.next
    # print("valor previous.next")
    # print(previous.next)
    # print("valor head.next")
    # print(head.next)
    
    return "Elemento removido."

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

print("Antes de remover:")
show(head)
print(remove(head, 40))
print("Após remover:")
show(head)
        