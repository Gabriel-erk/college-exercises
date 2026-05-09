class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def elementos_comuns(l1, l2):
    resultado = None
    ultimo_no = None

    atual1 = l1

    while atual1:
        atual2 = l2
        found = False

        while atual2:
            if atual1.data == atual2.data:
                found = True
                break
            atual2 = atual2.next

        if found:

            novo = Node(atual1.data)

            if resultado is None:
                resultado = novo
                ultimo_no = novo
            else:
                ultimo_no.next = novo
                ultimo_no = novo

        atual1 = atual1.next

    return resultado

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a1.next = a2
a2.next = a3

b1 = Node(2)
b2 = Node(3)
b3 = Node(4)
b1.next = b2
b2.next = b3

resultado = elementos_comuns(a1, b1)

atual = resultado
while atual:
    print(atual.data)
    atual = atual.next