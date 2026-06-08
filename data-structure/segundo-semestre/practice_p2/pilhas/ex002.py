class Stack:
    def __init__(self):
        self.items = []
    
    def registrar(self,item):
        self.items.append(item)
    
    def desfazer(self):
        print(f"Ação desfeita: {self.items.pop()}")
    
    def acoes_restantes(self):
        i = 0
        print("Ações restantes:")
        while i < len(self.items):
            print(self.items[i])
            i += 1

pilha = Stack()

pilha.registrar("Digitou: Olá")
pilha.registrar("Digitou: mundo")
pilha.registrar("Alterou fonte")

pilha.desfazer()

print("")

pilha.acoes_restantes()