# LIFO == last in last out (último a entrar, primeiro a sair)
class Stack:
    def __init__(self):
        self.elements = []
    
    # método push de uma stack (pilha) adiciona o novo que está entrando no FINAL (logo, fazendo com o que o último que entrou, se torne o topo da pilha, logo, ele será o PRIMEIRO a sair) 
    def push(self, item):
        self.elements.append(item)
    
    # esse pop basicamente executa um pop também, pois se o elemento vai SAIR da pilha, logo, ele está no TOPO, e se está no topo, ele é o ÚLTIMO, e o pop SEMPRE remove o úlimo de uma lista python
    def pop(self):
        return self.elements.pop()
    
    # retorna quem está no topo da pilha
    def peek(self):
        last = len(self.elements) - 1
        return self.elements[last]
    
    # diz se a pilha está vazia ou não
    def is_empty(self)->bool:
        if self.elements == []:
            return True
        return False
    
    def size(self)->int:
        return len(self.elements)
    # imprimir do topo para a base, pois, mostrará corretamente a ordem em que os elementos serão excluidos
    def show(self):
        i = 0
        while i < self.size():
            print(self.elements[i])
            i += 1
    
pilha = Stack()

i = 0
while i < 3:
    valor_pilha = int(input("Valor a se inserido: "))
    pilha.push(valor_pilha)
    i += 1

print(f"Topo: {pilha.peek()}")
print("Lista antes de remover um valor:")
pilha.show()
print(f"Valor removido: {pilha.pop()}")
print("Lista após remover um valor:")
pilha.show()
