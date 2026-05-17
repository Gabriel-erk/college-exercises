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
fila.enqueue("X")
fila.enqueue("Y")
fila.enqueue("Z")

print("Entrada: ", end=" ")
fila.show()

fila_preparados = Queue()
fila_preparados.enqueue(fila.dequeue())
fila_preparados.enqueue(fila.dequeue())
print("\n")

print("Saída (pedidos que foram preparados):")
fila_preparados.show()
print("\n")

print("Restantes (ainda não foram preparados):")
fila.show()

