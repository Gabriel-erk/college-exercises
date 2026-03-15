class Jogador:
    def __init__(self, nome_jogador: str):
        self.__nome_jogador = nome_jogador
    
    def get_nome(self)->str:
        return self.__nome_jogador

class Campeonato:
    def __init__(self):
        self.__nome_campeonato = "Campeonato do GB Lindo"
        self.ranking_campeonato = {}
        
    def get_nome_campeonato(self)->str:
        return self.__nome_campeonato

    def registrar_jogador(self, nome_jogador: str, pontuacao_inicial: int)->str:
        # se já não existir  o usuário adiciona no rank
        if nome_jogador not in self.ranking_campeonato:
            self.ranking_campeonato[nome_jogador] = pontuacao_inicial
            return f"O jogador: {nome_jogador} foi adicionado ao rank com sucesso!"
        else:
            return f"O jogador {nome_jogador} já está participando do rank."
    
    def add_pontos_jogador_existente(self, nome_jogador:str, pontuacao_a_adicionar: int)->str:
        if nome_jogador in self.ranking_campeonato:
            self.ranking_campeonato[nome_jogador] += pontuacao_a_adicionar
            return f"Foram adicionados {pontuacao_a_adicionar} pontos ao jogador: {nome_jogador}."
        else:
            return f"Pontos não foram adicionados, jogador não encontrado."
    
    def get_pontos_jogador_especifico(self, nome_jogador: str)->str:
        if nome_jogador in self.ranking_campeonato:
            return f"Jogador: {nome_jogador} - Pontos: {self.ranking_campeonato[nome_jogador]}."
        else:
            return f"Jogador {nome_jogador} não encontrado."
    
    def mostrar_jogadores_e_pontuacoes(self)->None:
        for jogador in self.ranking_campeonato:
            print(f"Jogador: {jogador} - Pontuação: {self.ranking_campeonato[jogador]}")
    
    def maior_pontuacao(self)->str:
        maior_jogador = ""
        maior_pontuacao = 0
        
        for jogador in self.ranking_campeonato:
            if self.ranking_campeonato[jogador] > maior_pontuacao:
                maior_jogador = jogador
                maior_pontuacao = self.ranking_campeonato[jogador]
        return f"Jogador: {maior_jogador} - Pontuação: {maior_pontuacao}"
    
    # objetivo deset método é retornar um dicionário contendo os jogadores, do maior ao menor baseado em sua pontuação
    def ranking_ordenado(self) -> dict:

        dicionario_ordenado = {}

        while len(dicionario_ordenado) < len(self.ranking_campeonato):

            maior_jogador = ""
            maior_pontuacao = 0

            for jogador in self.ranking_campeonato:

                if jogador not in dicionario_ordenado:
                    if self.ranking_campeonato[jogador] > maior_pontuacao:
                        maior_jogador = jogador
                        maior_pontuacao = self.ranking_campeonato[jogador]
            dicionario_ordenado[maior_jogador] = maior_pontuacao

        return dicionario_ordenado

jogador_um = Jogador("Jorge")
jogador_dois = Jogador("pierre")
jogador_tres = Jogador("giorno")
jogador_quatro = Jogador("saskeeee")
jogador_cinco = Jogador("dio")
jogador_seis = Jogador("felca")
ranking = Campeonato()

print(f"Campeonato: {ranking.get_nome_campeonato()}")

print("=== Criando jogadores ===")
print(ranking.registrar_jogador(jogador_um.get_nome(), 1000))
print(ranking.registrar_jogador(jogador_dois.get_nome(), 10))
print(ranking.registrar_jogador(jogador_tres.get_nome(), 25))
print(ranking.registrar_jogador(jogador_quatro.get_nome(), 800))
print(ranking.registrar_jogador(jogador_cinco.get_nome(), 1100))
print(ranking.registrar_jogador(jogador_seis.get_nome(), 9999999))

print("")
print("=== Adicionando pontos a jogador existente ===")
print(ranking.add_pontos_jogador_existente(jogador_um.get_nome(), 10))

print("")
print("=== Pegando pontos jogador específico ===")
print(ranking.get_pontos_jogador_especifico(jogador_dois.get_nome()))

print("")
print("=== Listando todos os jogadores ===")
ranking.mostrar_jogadores_e_pontuacoes()

print("")
print("=== Maior Pontuação ===")
print(ranking.maior_pontuacao())

print("")
print("=== Ranking Ordenado ===")

dicionario_ordenado = ranking.ranking_ordenado()
print(dicionario_ordenado)
contador = 1
for jogador in dicionario_ordenado:
    print(f"{contador} - {jogador}, {dicionario_ordenado[jogador]} pontos. ")
    contador += 1
