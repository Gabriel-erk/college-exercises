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
# primeir a entrar - ultimo indice
fila.enqueue("Ana")
# segundo a entrar 
fila.enqueue("Bruno")
# terceiro a entrar
fila.enqueue("Carlos")
# quarto a entrar - até o momento, ultimo, logo, indice 0
fila.enqueue("Diana")


print("Entrada:", end=" ")
fila.show()

fila_atendidos = Queue()
# atendendo primeiro da fila, logo, processando o ultimo indice (baseado no conceito de filas) - atendendo == Ana (primeira a entrar)
fila_atendidos.enqueue(fila.dequeue())
# atendendo outro, como ja realizei um atendimento antes, o proximo é o primeiro pois como atendi o anterior, ele foi removido da fila, logo o segundo a entrar se torna o primeiro, o que faz com que, o ultimo indice agora seja o equivalente oq esta na fila a mais tempo, logo ele é o mais próximo de sair (se tornou o primeiro da fila pra resumir), meu método dequeue remove o último indice == o que está na fila a mais tempo, logo é o mais próximo a sair
fila_atendidos.enqueue(fila.dequeue())
print("\n")

print("Saída:", end = " ")
fila_atendidos.show()
print("\n")

print("Restante:", end =" ")
fila.show()

