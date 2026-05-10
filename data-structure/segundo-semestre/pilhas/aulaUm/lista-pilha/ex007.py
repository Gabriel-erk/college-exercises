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

pilha_torre_blocos = Stack()

pilha_torre_blocos.push(5)
pilha_torre_blocos.push(3)
pilha_torre_blocos.push(8)
pilha_torre_blocos.push(2)

print("Pilha inicial:", end=" ")
pilha_torre_blocos.show()

print(f"Removido: {pilha_torre_blocos.pop()}")
print("Pilha final:", end=" ")
pilha_torre_blocos.show()