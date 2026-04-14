class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class OrderedList:
    def __init__(self):
        self.head = None

    def add_ordenado(self, valor_a_adicionar):
        novo_no = Node(valor_a_adicionar)
        if self.head == None:
            head = novo_no
        
        found = False
        previous = None
        
        while self.head is not None:
            if self.head.data < valor_a_adicionar:
                found = True
                break
            previous = self.head
            self.head = self.head.next

        if found == False:
            return head
        
        self.head.next = valor_a_adicionar    
        return head
    
    def show(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

lista_ordenada = OrderedList()
lista_ordenada.add_ordenado(10)
lista_ordenada.show()
            