class Stack:
    def __init__(self):
        self.elements = []
        self.current_page = ""
    
    def is_empty(self):
        return self.elements == []
    
    def push(self, item):
        self.current_page = item
        self.elements.append(item)
        
        print(f"Acessar {item}")
    
    def pop(self):
        self.elements.pop()
        print("Voltar")

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

pilha.push("A")
pilha.push("B")
pilha.push("C")
pilha.pop()
pilha.push("D")

print(f"Saída: página atual == {pilha.current_page}")
print("histórico =", end=" ")
pilha.show()