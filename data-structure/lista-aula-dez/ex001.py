# limpeza de dados duplicados

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # para remover um valor duplicado, eu preciso primeiramente pegar algum valor
    # em seguida, comparo se aquele valor está presente na lista mais de uma vez, sempre salvando o valor anterior a ele (previous) para fazer a ponte do valor antigo do que quero remover com o proximo do valor que será removido
    # caso eu encontre outro valor igual a ele, aponto o valor anterior a ele (previous) para o PRÓXIMO do meu valor atual (valor repetido), assim removendo esse outro da lista
    # def remover_duplicados(self):
        
                    
    

n1 = Node(5)
n2 = Node(3)
n3 = Node(5)
n4 = Node(2)
n5 = Node(3)
n6 = Node(1)

head = n1

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6