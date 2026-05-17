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

# não consegui entender direito o enunciado do exercício então apenas tentei assumir alguma linha de raciocínio e realizar o exercício tentando atender as condicões do enunciado proposto (operacões definidas no código/fila dinâmica com operacões)
fila = ["A", "B", "C"]
atendidos = []

# operações interpretei como o ato de remover/adicionar alguém
fila.append("D")
atendidos.append(fila.pop(0))

fila.append("E")
atendidos.append(fila.pop(0))

print("Atendidos:")
print(atendidos)

print("Restantes:")
print(fila)
