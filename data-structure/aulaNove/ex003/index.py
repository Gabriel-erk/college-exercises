class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


def buscar(head, alvo):
    atual = head

    while atual is not None:
        if atual.valor == alvo:
            return True
        atual = atual.proximo

    return False


# montagem da lista: 4 -> 9 -> 12 -> 18
n1 = Node(4)
n2 = Node(9)
n3 = Node(12)
n4 = Node(18)

n1.proximo = n2
n2.proximo = n3
n3.proximo = n4

print(buscar(n1, 12))  # True
print(buscar(n1, 5))   # False