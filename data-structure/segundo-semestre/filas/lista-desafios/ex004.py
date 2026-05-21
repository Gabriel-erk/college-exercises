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

    def enqueue_urgente(self, item):

        self.elements.append(item)

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

fila.enqueue("A(normal)")
fila.enqueue("B(normal)")
fila.enqueue_urgente("C(urgente)")

print("Fila de tarefas:", end=" ")
fila.show()

print(" ")
print("Ordem de execução:", end=" ")

while fila.size() > 0:
    # primeiro vai sair o C (pois entrou de forma urgente, depois irà remover por "ordem de chegada")
    print(fila.dequeue(), end=" ")