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

palavra = input("Digite uma palavra: ")
lista_caracteres_palavra = list(palavra)

pilha = Stack()

while lista_caracteres_palavra != [] :
    pilha.push(lista_caracteres_palavra.pop())

palavra_inversa = ""
indice = 0

while indice < pilha.size():
    palavra_inversa += pilha.elements[indice]
    indice += 1

if palavra == palavra_inversa:
    print("Palíndromo")
else:
    print("Não palíndromo")