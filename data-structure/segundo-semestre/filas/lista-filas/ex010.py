class Queue:
    def __init__(self):
        self.elements = []
        self.assentos_preenchidos = 0
    
    def is_empty(self):
        print("--- FILA ---")
        if self.elements == []:
            print("Fila vazia")
        else:
            print("Fila não está vazia")
        print("----------")

        return self.elements == []
    
    # def enqueue(self, item):
    #     self.elements.insert(0, item)
    
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
            
    def embarque_enqueue(self, item, capacidade_onibus = 6)->bool:
        if self.assentos_preenchidos < capacidade_onibus:
            self.elements.insert(0,item)
            self.assentos_preenchidos += 1

            return True
        else:
            return False

fila = Queue()
capacidade_onibus = int(input("Informe a capacidade de passageiros do ônibus: "))
limite_passageiros = int(input("Informe quantos passageiros pretendem entrar: "))

print(f"Entrada: {limite_passageiros} pessoas.")
i = 0
embarcados = 0
restantes = 0
while i < limite_passageiros:
    if fila.embarque_enqueue(f"Passageiro {i + 1}", capacidade_onibus):
        embarcados += 1
    else:
        restantes += 1
    i += 1

print(f"Saída: {embarcados} embarcam, {restantes} aguardam.")