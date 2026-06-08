class Stack:
    def __init__(self):
        self.items = []
    
    def acessar(self, item):
        self.items.append(item)
    
    def voltar(self):
        return self.items.pop()

    def pagina_atual(self):
        last = len(self.items) - 1
        print(f"Página atual: {self.items[last]}")

    def historico(self):
        i = 0
        print("Histórico:", end=" ")
        while i < len(self.items):
            if i + 1 == len(self.items):
                print(self.items[i])
            else:
                print(self.items[i], end=" -> ")
            i += 1

pilha = Stack()

pilha.acessar("google.com")
pilha.acessar("unimar.br")
pilha.acessar("moodle.unimar.br")

pilha.voltar()

pilha.pagina_atual()

pilha.historico()