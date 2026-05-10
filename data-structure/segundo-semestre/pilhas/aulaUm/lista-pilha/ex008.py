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

pilha_acoes = Stack()

pilha_acoes.push("Digitar A")
pilha_acoes.push("Digitar B")
pilha_acoes.push("Apagar")
pilha_acoes.push("Colar")

print("Pilha inicial:", end=" ")
pilha_acoes.show()

pilha_acoes_desfeitas = Stack()

pilha_acoes_desfeitas.push(pilha_acoes.pop())
pilha_acoes_desfeitas.push(pilha_acoes.pop())

print("Desfeitas:", end=" ")
pilha_acoes_desfeitas.show()

print("Pilha final:", end=" ")
pilha_acoes.show()
