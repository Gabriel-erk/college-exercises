class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

def elementos_comuns(l1, l2):
    resultado = None
    ultimo_no = None

    atual1 = l1

    while atual1:
        atual2 = l2
        encontrado = False

        while atual2:
            if atual1.valor == atual2.valor:
                encontrado = True
                break
            atual2 = atual2.next

        if encontrado:

            novo = Node(atual1.valor)

            if resultado is None:
                resultado = novo
                ultimo_no = novo
            else:
                pass

        atual1 = atual1.next

    return resultado