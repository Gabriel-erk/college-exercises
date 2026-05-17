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
i = 0

while i < 4:
    fila.enqueue(f"doc{i + 1}")
    i += 1

print("Entrada:", end=" ")
fila.show()
print("\n")

print("Saída:", end=" ")
fila.show()