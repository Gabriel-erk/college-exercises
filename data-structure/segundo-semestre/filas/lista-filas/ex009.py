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

fila.enqueue(5)
fila.enqueue(3)
fila.enqueue(8)
fila.enqueue(2)

print("Entrada:", end="")
fila.show_from_start()

i = 0
soma_valores = 0

while i < fila.size():
    soma_valores += fila.elements[i]
    i += 1
print(" ")

print(f"Saída: total={soma_valores}")