class Documento:
    def __init__(self, nome, usuario, quantidade_paginas):
        self.nome = nome
        self.usuario = usuario
        self.quantidade_paginas = quantidade_paginas

class Queue:
    def __init__(self):
        self.elements = []
    
    def adicionar_documento(self, item):
        self.elements.insert(0, item)
    
    def imprimir(self):
        return self.elements.pop()
    
    def aguardando_impressao(self):
        i = len(self.elements) - 1
        while i >= 0:
            if i - 1 == -1:
                print(self.elements[i])
            else:
                print(self.elements[i], end=" -> ")
            i -= 1

doc1 = Documento("prova.pdf", "Professor", 4)
doc2 = Documento("trabalho.docx", "Aluno", 8)

fila = Queue()

fila.adicionar_documento(doc1)
fila.adicionar_documento(doc2)

imprimindo = fila.imprimir()

print(f"Imprimindo: {imprimindo.nome}")
print(f"Usuário: {imprimindo.usuario}")
print(f"Páginas: {imprimindo.quantidade_paginas}")

