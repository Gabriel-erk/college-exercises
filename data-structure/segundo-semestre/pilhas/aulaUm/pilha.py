class Stack:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return self.elements == []
    
    def push(self, item):
        self.elements.append(item)
    
    def pop(self):
        return self.elements.append(item)

    def peek(self):
        return self.elements[len(self.elements)-1]

    def size(self):
        return len(self.elements)
    
    def show(self):
        if self.elements != []:
            indice = len(self.elements) - 1 
            topo = len(self.elements) - 1 

            print("--- PILHA ---")
            while indice >= 0:
                if topo == indice:
                    print(f"| {self.elements[indice]} | <- TOPO")
                else:
                    print(f"| {self.elements[indice]} |")
                indice -= 1
            print("----------")
        else:
            print("Lista vazia.")


pilha = Stack()

# pilha.push(10)
# pilha.push(20)
# pilha.push(30)

pilha.show()