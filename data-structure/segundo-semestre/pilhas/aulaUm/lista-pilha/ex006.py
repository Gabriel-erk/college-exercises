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

pilha.push(10)
pilha.push(20)
pilha.push(30)

print("Pilha:", end=" ")
pilha.show()

print(f"Removido: {pilha.pop()}")

indice = 0
soma_valores_pilha = 0
while indice < pilha.size():
    soma_valores_pilha += pilha.elements[indice]
    indice += 1

print(f"Soma restante: {soma_valores_pilha}")
