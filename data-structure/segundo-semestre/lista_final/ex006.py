class Pedido:
    def __init__(self, codigo, cliente, valor_total):
        self.codigo = codigo
        self.cliente = cliente
        self.valor_total = valor_total

class Queue:
    def __init__(self):
        self.elements = []
    
    def adicionar_pedido(self, item):
        self.elements.insert(0, item)
    
    def processar_pedido(self):
        first_out = len(self.elements) - 1
        
        print(f"Pedido processado: {self.elements[first_out].codigo}")
        print(f"Cliente: {self.elements[first_out].cliente}")
        print(f"Valor: {self.elements[first_out].valor_total}")
        
        self.elements.pop()
        
        print(f"Pedidos pendentes: {self.pedidos_pendentes()}")
        
    def pedidos_pendentes(self):
        return len(self.elements)

pedido1 = Pedido(101, "Lucas", 250.00)
pedido2 = Pedido(102, "Bianca", 120.50)

fila = Queue()

fila.adicionar_pedido(pedido1)
fila.adicionar_pedido(pedido2)

fila.processar_pedido()
        