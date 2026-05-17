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
    fila.enqueue(f"Paricipante {i + 1}")
    i += 1

print("Entrada:", end=" ")
fila.show_from_start()

# print("tentativa de simular rodadas")
fila_circular = Queue()
first_element = fila.size() - 1
i = 0
rodadas = 5

while i < rodadas:
    if first_element >= 0:
        fila_circular.enqueue(fila.elements[first_element])
        if first_element == 0:
            first_element = fila.size() - 1
        else:
            first_element -= 1
    i += 1
print(" ")

print("Saída:", end=" ")
fila_circular.show_from_start()