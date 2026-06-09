class Queue:
    def __init__(self):
        self.elements = []
    
    def entrar_na_fila(self, item):
        self.elements.insert(0, item)
    
    def atender(self):
        return self.elements.pop()
    
    def show(self):
        i = len(self.elements) - 1
        while i >= 0:
            if i - 1 == -1:
                print(self.elements[i])
            else:
                print(self.elements[i], end=" -> ")
            i -= 1
    
fila = Queue()  
  
fila.entrar_na_fila("Ana")
fila.entrar_na_fila("Carlos")
fila.entrar_na_fila("Marina")

print(f"Paciente atendido: {fila.atender()}")

print("Fila atual: ", end=" ")
fila.show()



