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

fila = Queue()

limite_chamados = int(input("Informe o limite de chamados: "))
i = 0

while i < limite_chamados:
    chamado = int(input(f"Valor do chamado {i + 1}: "))
    fila.enqueue(chamado)
    i += 1

print("Entrada:", end=" ")
fila.show()
print("\n")

fila_atendidos = Queue()
indice_atendidos = 0
while fila.size() >= 3:
    fila_atendidos.enqueue(fila.dequeue())
    indice_atendidos += 1 

print("Saída:", end=" ")
fila_atendidos.show()
print("\n")

print("Restante:", end=" ")
fila.show()


