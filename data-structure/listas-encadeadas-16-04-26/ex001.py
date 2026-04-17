class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def remover_duplicados(head):
    current = head

    while current:
        atual2 = current
        while atual2.next:
            if atual2.next.data == current.data:
                atual2.next = atual2.next.next  
            else:
                atual2 = atual2.next
        current = current.next

    return head