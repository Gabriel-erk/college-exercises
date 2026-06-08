class Queue:
    def __init__(self):
        self.items = []
    
    def adicionar_pedido(self, item):
        self.items.insert(0, item)
    
    def processar_pedido(self):
        return self.items.pop()
    
class Pedido:
    def __init__(self, codigo, cliente, valor_total):
        self.codigo = codigo
        self.cliente = cliente
        self.valor_total = valor_total

fila = Queue()

pedido1 = Pedido(101, "Lucas", 250.00)
pedido2 = Pedido(102, "Bianca", 120.50)

fila.adicionar_pedido(pedido1)
fila.adicionar_pedido(pedido2)

pedido_processado = fila.processar_pedido()  
print(f"Pedido processado: {pedido_processado.codigo}")
print(f"Cliente: {pedido_processado.cliente}")
print(f"Valor: {pedido_processado.valor_total}")
print(f"Pedidos restantes: {len(fila.items)}")


  