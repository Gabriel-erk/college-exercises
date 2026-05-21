class Stack:

    def __init__(self):
        self.elements = []

    def push(self, item):

        self.elements.append(item)

    def pop(self):

        return self.elements.pop()

    def is_empty(self):

        return len(self.elements) == 0


expressao = "( ( ) [ ] { } )"

pilha = Stack()

valida = True

for caractere in expressao:

    if caractere == "(" or caractere == "[" or caractere == "{":

        pilha.push(caractere)

    elif caractere == ")" or caractere == "]" or caractere == "}":

        if pilha.is_empty():

            valida = False
            break

        topo = pilha.pop()

        if caractere == ")" and topo != "(":
            valida = False

        elif caractere == "]" and topo != "[":
            valida = False

        elif caractere == "}" and topo != "{":
            valida = False


if not pilha.is_empty():
    valida = False

if valida:
    print("válida")

else:
    print("inválida")