class Stack:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return self.elements == []
    
    def push(self, item):
        self.elements.append(item)
    
    def pop(self):
        return self.elements.pop()
    
    def peek(self):
        return self.elements[len(self.elements)-1]

    def size(self):
        return len(self.elements)
    
    def show(self):
        if self.elements != []:
            print(self.elements)
        else:
            print("Lista vazia.")

pilha_original = Stack()

# pilha_original.append(1)
# pilha_original.append(2)
# pilha_original.append(3)
# pilha_original.append(4)
# pilha_original.append(5)
# pilha_original.append(6)

indice = 0
while pilha_original.size() < 6:
    pilha_original.push(indice + 1)
    indice += 1

print("Entrada:", end=" ")
pilha_original.show()

i = 0
pilha_pares = Stack()
while i < pilha_original.size():
    if pilha_original.elements[i] % 2 == 0:
        pilha_pares.push(pilha_original.elements.pop(i))
    i += 1

print("Saida esperada:", end=" ")
pilha_pares.show()
