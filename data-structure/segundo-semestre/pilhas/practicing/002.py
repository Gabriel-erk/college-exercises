class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, item):
        self.elements.append(item)
    
    def peek(self):
        last = self.elements - 1
        return self.elements[last]
    
    def pop(self):
        if self.is_empty() == False:
            return self.elements.pop()
    
    def is_empty(self)->bool:
        if self.elements == []:
            return True
        return False
    
    def size(self):
        return len(self.elements)
    
    def show(self):
        i = 0
        while i < self.size():
            print(self.elements[i])
            i += 1
    # imprimir do topo para a base, pois, mostrará corretamente a ordem em que os elementos serão excluidos
    def show_from_start(self):
        i = self.size() - 1
        while i >= 0:
            print(self.elements[i])
            i -= 1

pilha = Stack()
caracteres = list("python")

i = 0
while i < len(caracteres):
    pilha.push(caracteres[i])
    i += 1

j = pilha.size() - 1
palavra_desempilhada = ""
while j > 0:
    palavra_desempilhada += pilha.pop()
    i -+ 1

print(palavra_desempilhada)