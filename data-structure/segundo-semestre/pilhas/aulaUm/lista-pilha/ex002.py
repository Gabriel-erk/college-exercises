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

pilha_livros = Stack()

pilha_livros.push("Python")
pilha_livros.push("Algoritmos")
pilha_livros.push("Estruturas de Dados")

print("Pilha:", end=" ")
pilha_livros.show()
print(f"Topo inicial: {pilha_livros.peek()}")
print(f"Removido: {pilha_livros.pop()}")
print(f"Novo topo: {pilha_livros.peek()}")