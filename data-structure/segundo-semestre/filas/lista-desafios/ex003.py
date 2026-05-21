class Queue:

    def __init__(self):
        self.elements = []
        self.atendidos = []

    def enqueue(self, item):
        self.elements.insert(0, item)

    def atender(self):

        if len(self.elements) > 0:

            paciente = self.elements.pop()

            self.atendidos.insert(0, paciente)

    def faltar(self):

        if len(self.elements) > 0:

            paciente = self.elements.pop()

            self.elements.insert(0, paciente)

    def show_from_start(self):

        indice = len(self.elements) - 1

        while indice >= 0:
            print(self.elements[indice], end=" ")
            indice -= 1

    def show_atendidos_from_start(self):

        indice = len(self.atendidos) - 1

        while indice >= 0:
            print(self.atendidos[indice], end=" ")
            indice -= 1


fila = Queue()

fila.enqueue("A")
fila.enqueue("B")
fila.enqueue("C")

print("Fila:", end=" ")
fila.show_from_start()

print(" ")

quantidade_eventos = int(input("Informe quantos eventos irão acontecer: "))

eventos_validos = ["atender", "faltar"]
eventos_usuario = []

i = 0

while i < quantidade_eventos:

    evento = input("Informe o evento (atender, faltar): ")

    if evento not in eventos_validos:
        print("Escolha inválida, tente novamente.")

    else:
        eventos_usuario.append(evento)
        i += 1

print(" ")

print("Eventos:", end=" ")

indice = 0

while indice < len(eventos_usuario):

    evento = eventos_usuario[indice]

    print(evento, end=" ")

    if evento == "atender":
        fila.atender()

    elif evento == "faltar":
        fila.faltar()

    indice += 1

print(" ")
print(" ")

print("Saída: atendidos=", end="")
fila.show_atendidos_from_start()

print(" ")
print("fila=", end="")
fila.show_from_start()