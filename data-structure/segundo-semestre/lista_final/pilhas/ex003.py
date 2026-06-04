class Stack:
    def __init__(self):
        self.elements = []
    
    def registrar(self, item):
        self.elements.append(item)
    
    def desfazer(self):
        return self.elements.pop()
        
    def acoes_registradas(self):
        i = 0
        while i < len(self.elements):
            print(self.elements[i])
            i += 1
    
pilha = Stack()
pilha.registrar("Digitou: Olá")
pilha.registrar("Digitou: mundo")
pilha.registrar("Alterou fonte")

print(f"Ação desfeita: {pilha.desfazer()}")
print("Ações restantes:")
pilha.acoes_registradas()
