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

expressao_matematica = input("Digite uma expressão matemática: ")
lista_caracteres_expressao_matematica = list(expressao_matematica)

pilha = Stack()

indice = 0
while indice < len(lista_caracteres_expressao_matematica):
    if lista_caracteres_expressao_matematica[indice] == "(":
        pilha.push(lista_caracteres_expressao_matematica[indice].pop())

#tentei aqui mas esse não consegui entender nada professor