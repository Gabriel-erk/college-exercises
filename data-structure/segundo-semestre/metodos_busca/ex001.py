class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome

def busca_binaria(lista, alvo):
    # para saber o meio da lista, preciso saber o inicio e o fim da lista antes de comećar a busca
    inicio = 0
    fim = len(lista) - 1

    # uso essa condićão pois caso tenha um cenário em que o valor de inicio é MAIOR que o valor do indice final, deve ser um índice inválido ou já olhamos todos os índices e não achamos o valor que procuravamos
    while inicio <= fim:
        # calculo do meio da lista, cortando a parte decimal com: //
        meio = (inicio + fim) // 2

        # se a lista no indice que representa o meio dela for igual ao valor que procuramos, já retornamos pois achamos o valor procurado
        if lista[meio] == alvo:
            return meio

        # se o valor alvo for menor que o valor que está no meio da lista
        if alvo < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1

aluno1 = Aluno(2024001, "Ana")
aluno2 = Aluno(2024002, "Bruno")
aluno3 = Aluno(2024003, "Carla")
aluno4 = Aluno(2024004, "Daniel")
aluno5 = Aluno(2024005, "Eduarda")

alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

ra_buscado = 2024004