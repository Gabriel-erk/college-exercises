class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


def contar(head, alvo):
    atual = head
    contador = 0

    while atual is not None:
        if atual.valor == alvo:
            contador += 1
        atual = atual.proximo

    return contador



n1 = Node(3)
n2 = Node(6)
n3 = Node(3)
n4 = Node(9)
n5 = Node(3)
n6 = Node(12)

n1.proximo = n2
n2.proximo = n3
n3.proximo = n4
n4.proximo = n5
n5.proximo = n6

print(contar(n1, 3))  
print(contar(n1, 8))  