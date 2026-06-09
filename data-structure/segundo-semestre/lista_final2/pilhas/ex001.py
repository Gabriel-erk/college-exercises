class Stack():
    def __init__(self):
        self.elements = []
    
    def acessar(self, item):
        self.elements.append(item)

    def voltar(self):
        self.elements.pop()
        
    def pagina_atual(self):
        last = len(self.elements) - 1
        return self.elements[last]
    
    def historico(self):
        i = 0
        while i < len(self.elements):
            if i + 1 == len(self.elements):
                print(self.elements[i])
            else:
                print(self.elements[i], end=" -> ")
            i += 1

pilha = Stack()

pilha.acessar("google.com")
pilha.acessar("unimar.br")
pilha.acessar("moodle.unimar.br")
pilha.voltar()

print(f"Página atual: {pilha.pagina_atual()}")
print("Histórico: ", end=" ")
pilha.historico()




