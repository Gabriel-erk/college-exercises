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
    
    def show_from_start(self):
        indice = len(self.elements) - 1
        
        while indice >= 0:
            print(self.elements[indice], end=" ")
            indice -= 1
    
    def show(self):
        indice = 0
        
        while indice < len(self.elements):
            print(self.elements[indice], end=" ")
            indice += 1

fila = Queue()

i = 0

while i < 3:
    fila.enqueue(f"Participante {i + 1}")
    i += 1

print("Entrada:", end=" ")
fila.show_from_start()

fila_atendidos = Queue()
indice_atendido = fila.size() - 1

while indice_atendido >= 0:
    fila_atendidos.enqueue(fila.dequeue())
    indice_atendido -= 1
print("\n")

print("Saída:", end=" ")
fila_atendidos.show_from_start()