class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class HistoricoNavegacao:
    def __init__(self):
        self.inicio = None
        self.atual = None

    def registrar_acesso(self, conteudo):
        new = Node(conteudo)

        if self.inicio is None:
            self.inicio = new
            self.atual = new
            return

        self.atual.next = None

        new.previous = self.atual
        self.atual.next = new
        self.atual = new

    def voltar(self):
        if self.atual and self.atual.previous:
            self.atual = self.atual.previous

    def avancar(self):
        if self.atual and self.atual.next:
            self.atual = self.atual.next

    def mostrar_historico(self):
        temp = self.inicio
        while temp:
            if temp == self.atual:
                print(f"-> {temp.data} (ATUAL)")
            else:
                print(temp.data)
            temp = temp.next

    def mostrar_atual(self):
        if self.atual:
            print(f"Conteúdo atual: {self.atual.data}")

    def contar_conteudos(self):
        count = 0
        temp = self.inicio
        while temp:
            count += 1
            temp = temp.next
        return count

    def buscar_conteudo(self, texto):
        temp = self.inicio
        while temp:
            if temp.data == texto:
                return True
            temp = temp.next
        return False