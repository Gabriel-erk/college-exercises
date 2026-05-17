class Queue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        print("--- FILA ---")
        if self.elements == []:
            print("Fila vazia")
        else:
            print("Fila não está vazia")
        print("----------")

        return self.elements == []
    
    def enqueue(self, item):
        self.elements.insert(0, item)
    
    def dequeue(self):
        return self.elements.pop()
    
    def size(self):
        return len(self.elements)
    
    def show(self):
        indice = len(self.elements) - 1
        
        while indice >= 0:
            print(self.elements[indice], end=" ")
            indice -= 1

indice = 0
fila = Queue()

while indice < 5:
    fila.enqueue(f"Aluno {indice + 1}")
    indice += 1

print("Entrada:", end=" ")
fila.show()

indice_atendidos = fila.size() - 1
fila_atendidos = Queue()
iteracoes = 0

while iteracoes < 3:
    fila_atendidos.enqueue(fila.dequeue())
    iteracoes += 1
print("\n")

print("Saída:", end=" ")
fila_atendidos.show()
print("\n")

print("Restante:", end=" ")
fila.show()
