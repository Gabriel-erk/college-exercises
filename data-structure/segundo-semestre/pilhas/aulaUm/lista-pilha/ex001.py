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

pilha = Stack()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.push(4)

print("Pilha inicial:", end=" ")
pilha.show()

pilha_removidos = Stack()
pilha_removidos.push(pilha.pop())
pilha_removidos.push(pilha.pop())

print("Remoções:", end=" ")
pilha_removidos.show()

print(f"Último removido: {pilha_removidos.peek()}")
print("Pilha final:", end=" ")
pilha.show()