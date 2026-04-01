class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


def mostrar_lista(head):
    atual = head
    while atual is not None:
        print(atual.valor)
        atual = atual.proximo


def inserir_fim(head, valor):
    novo = Node(valor)

    if head is None:
        return novo

    atual = head
    while atual.proximo is not None:
        atual = atual.proximo

    atual.proximo = novo
    return head


def buscar(head, alvo):
    atual = head
    while atual is not None:
        if atual.valor == alvo:
            return True
        atual = atual.proximo
    return False


def contar(head, alvo):
    atual = head
    contador = 0

    while atual is not None:
        if atual.valor == alvo:
            contador += 1
        atual = atual.proximo

    return contador

n1 = Node(101)
n2 = Node(205)
n3 = Node(101)
n4 = Node(330)

n1.proximo = n2
n2.proximo = n3
n3.proximo = n4

print("Lista inicial:")
mostrar_lista(n1)

n1 = inserir_fim(n1, 450)

print("Produto 205 existe?", buscar(n1, 205))

print("Quantidade de 101:", contar(n1, 101))

print("Lista final:")
mostrar_lista(n1)