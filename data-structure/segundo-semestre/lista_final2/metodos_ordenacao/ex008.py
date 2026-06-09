def selection_sort_decrescente(lista) -> list:
    tamanho = len(lista)
    atual = 0

    while atual < tamanho - 1:
        indice_maior = atual
        i = atual + 1

        while i < tamanho:
            if lista[i].pontuacao > lista[indice_maior].pontuacao:
                indice_maior = i
            i += 1

        if indice_maior != atual:
            aux = lista[atual]
            lista[atual] = lista[indice_maior]
            lista[indice_maior] = aux

        atual += 1

    return lista

class Jogador:
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao


jogadores = [
    Jogador("Ana", 120),
    Jogador("Carlos", 90),
    Jogador("Marina", 150),
    Jogador("João", 110)
]

selection_sort_decrescente(jogadores)

print("Ranking:")

for i, jogador in enumerate(jogadores, start=1):
    print(f"{i}º lugar: {jogador.nome} - {jogador.pontuacao} pontos")