class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def busca_desordenada(head, valor):
    passos = 0
    atual = head

    while atual:
        passos += 1
        if atual.valor == valor:
            return True, passos
        atual = atual.next

    return False, passos


def busca_ordenada(head, valor):
    passos = 0
    current = head

    while current:
        passos += 1

        if current.valor == valor:
            return True, passos

        if current.valor > valor:
            return False, passos  

        current = current.next

    return False, passos