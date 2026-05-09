class Stack:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return self.elements == []
    
    def push(self, item):
        self.elements.append(item)
    
    def pop(self):
        return self.elements.pop()
    #retorna ultimo elemento, não tamanho da lista como eu pensava
    def peek(self):
        return self.elements[len(self.elements)-1]

    def size(self):
        return len(self.elements)
    
    def show(self):
        if self.elements != []:
            print(self.elements)
        else:
            print("Lista vazia.")
    
    # def reverse(self):
    #     indice = len(self.elements) - 1
    #     while indice >= 0:
    #         print(self.elements[indice])
    #         indice -= 1
            
pilha_letras = Stack()
palavra = input("Digite qualquer palavra: ")
# não fazia ideia de como converter cada caractere de uma string em uma posićão do array, então utilizei este método do python para isso
letras = list(palavra)
while letras != []:
    pilha_letras.push(letras.pop())

indice = 0
palavra_invertida = ""
while indice < len(pilha_letras.elements):
    palavra_invertida += pilha_letras.elements[indice]
    indice += 1
print(palavra_invertida)
