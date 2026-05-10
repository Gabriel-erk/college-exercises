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

pilha = Stack()

expressao = input("Digite a expressão: ")

valida = True

for caractere in expressao:

    if caractere == "(":
        pilha.push(caractere)

    elif caractere == ")":

        if pilha.is_empty():
            valida = False
            break

        pilha.pop()


if valida and pilha.is_empty():
    print("válida")
else:
    print("inválida")