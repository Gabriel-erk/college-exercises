class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Servico:
    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor


class Atendimento:
    def __init__(self, cliente):
        self.cliente = cliente
        self.servicos = []
        self.status = "pendente"

    def adicionar_servico(self, servico):
        self.servicos.append(servico)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def busca_sequencial(servicos, codigo):
    for servico in servicos:
        if servico.codigo == codigo:
            return servico

    return None

def selection_sort(servicos):

    tamanho = len(servicos)

    for atual in range(tamanho):

        indice_menor = atual

        for i in range(atual + 1, tamanho):

            if servicos[i].codigo < servicos[indice_menor].codigo:
                indice_menor = i

        servicos[atual], servicos[indice_menor] = (
            servicos[indice_menor],
            servicos[atual]
        )

def busca_binaria(servicos, codigo):

    inicio = 0
    fim = len(servicos) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        if servicos[meio].codigo == codigo:
            return servicos[meio]

        elif codigo < servicos[meio].codigo:
            fim = meio - 1

        else:
            inicio = meio + 1

    return None

def calcular_total(servicos):

    if len(servicos) == 0:
        return 0

    return servicos[0].valor + calcular_total(servicos[1:])

historico = Stack()
fila = Queue()

servicos = [
    Servico(301, "Formatação", 120),
    Servico(105, "Limpeza", 80),
    Servico(220, "Troca teclado", 150),
    Servico(410, "SSD", 250),
    Servico(180, "Diagnóstico", 50)
]

ana = Cliente("Ana", "111")
bruno = Cliente("Bruno", "222")

at1 = Atendimento(ana)
at2 = Atendimento(bruno)

fila.enqueue(at1)
historico.push("Ana entrou na fila")

fila.enqueue(at2)
historico.push("Bruno entrou na fila")

atual = fila.dequeue()

atual.status = "em atendimento"

historico.push(
    f"Atendimento de {atual.cliente.nome} iniciado"
)

servico = busca_sequencial(servicos, 220)

selection_sort(servicos)

servico2 = busca_binaria(servicos, 180)

atual.adicionar_servico(servico)
historico.push("Serviço adicionado")

atual.adicionar_servico(servico2)
historico.push("Serviço adicionado")

total = calcular_total(atual.servicos)

atual.status = "finalizado"

historico.push(
    f"Atendimento de {atual.cliente.nome} finalizado"
)

print(atual.cliente.nome)
print(atual.cliente.cpf)

for servico in atual.servicos:
    print(servico.descricao)

print(total)

print(atual.status)

print("Última ação desfeita:")
print(historico.pop())