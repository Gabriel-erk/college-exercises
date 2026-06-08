class Documento:
    def __init__(self, nome, usuario, quantidade_paginas):
        self.nome = nome
        self.usuario = usuario
        self.quantidade_paginas = quantidade_paginas

class Queue:
    def __init__(self):
        self.items = []
    
    def adicionar_documento(self,item):
        self.items.insert(0, item)
    
    def imprimir(self):
        return self.items.pop()

doc1 = Documento("prova.pdf", "Professor", 4)
doc2 = Documento("trabalho.docx", "Aluno", 8)

fila = Queue()

fila.adicionar_documento(doc1)
fila.adicionar_documento(doc2)

documento_imprimido = fila.imprimir()

print(f"Imprimindo: {documento_imprimido.nome}")
print(f"Usuário: {documento_imprimido.usuario}")
print(f"Páginas: {documento_imprimido.quantidade_paginas}")


