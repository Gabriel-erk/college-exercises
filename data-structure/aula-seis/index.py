class Jogador:
    def __init__(self, nome_jogador: str):
        self.__nome_jogador = nome_jogador
    
    def get_nome(self)->str:
        return self.__nome_jogador

class Ranking:
    def __init__(self):
        self.__lista_jogadores = [] # 1 passo, inicializando o programa com uma lista vazia de jogadores
    
    # 2 passo, deve ser possivel adicionar jogadores ao final da lista (append faz isso em python)
    def add_jogadores_final_lista(self, nome_jogador: str)->None:
        # passando um objeto do tipo jogador para o final da lista
        self.__lista_jogadores.append(nome_jogador)
        print(f"Jogador: {nome_jogador} adicionado com sucesso ao final da lista!")
        self.mostrar_lista()
    
    # 3 passo, adicionar um jogador em uma posição desejada da lista - mas e se a posição informada não existir? (seguindo a lógica ele não pode adicionar, imagina ele colocar o valor 10000 sendo q a lista só tem 10 valores? terei que preencher ela até com posições vazias até 10000? é possível mas acho que não é o correto, então limitarei a essa regra de apenas posições existentes)
    def add_jogadores_posicao_especifica(self, posicao_desejada_lista: int, nome_jogador: str)->None:
        # caso o método abaixo retorne true, significa que foi passado um valor que NÃO está entre o primeiro e o último indice da lista (ou seja, é maior que a lista ou menor que ela, logo, sendo uma posição inválida), eu não adiciono e retorno uma msg pedindo um valor valido (e descrevendo qual seria o mesmo) assim, encerrando a execução do método
        if self.verifica_posicao_valida(posicao_desejada_lista) == False:
            print(f"Não foi possível adicionar o jogador: '{nome_jogador}' ao rankig, favor informa uma posição existente entre: 0 e {len(self.__lista_jogadores)} ou verificar se o ranking já não possui 10 jogadores.")
            self.mostrar_lista()
        else:
            # agora, se é valido a posição (ou seja, não é menor que zero e nao é maior que o tamanho da lista, pode adicionar)
            # se é uma posição válida, então já possui um jogador, então removo ele, mando para a última posição e na sua posição antiga (vulgo: posição escolhida pelo usuário) coloco o jogador recebido
            
            nome_jogador_excluido = self.__lista_jogadores[posicao_desejada_lista]
            self.__lista_jogadores.pop(posicao_desejada_lista)
            
            self.__lista_jogadores.insert(posicao_desejada_lista, nome_jogador)
            print(f"Jogador: {nome_jogador} adicionado com sucesso na posição: {posicao_desejada_lista} no lugar do jogador: {nome_jogador_excluido}.")
            self.__lista_jogadores.append(nome_jogador_excluido)
            self.mostrar_lista()
    
    # 4 passo, remover um jogador a partir do seu índice (como o python já reorganiza os indices após uma remoção, não preciso "reordenar" como no php)
    def remover_jogador_pelo_indice(self, posicao_desejada_lista: int)->None:
        # não repeti a condição do if mas repeti o conteúdo pqp
        if self.verifica_posicao_valida(posicao_desejada_lista) == False:
            print(f"Não foi possível adicionar o jogador ao rankig, favor informa uma posição existente entre: 0 e {len(self.__lista_jogadores)} ou verificar se o ranking já não possui 10 jogadores.")
            self.mostrar_lista()
        else:
            nome_jogador_excluido = self.__lista_jogadores[posicao_desejada_lista]
            self.__lista_jogadores.pop(posicao_desejada_lista)
            print(f"Jogador: {nome_jogador_excluido} removido com sucesso do ranking!")
            self.mostrar_lista()
    
    # função para evitar repetição de código, pois usaria essa mesma lógica em 2 métodos (aproveitando e já tratrando o 1 passo do desafio extra não permitindo um indíce inválido ao remover o jogador e o 2 passo não permitindo que ultrapasse 10 jogadores)
    def verifica_posicao_valida(self, posicao_desejada_lista)->bool:
        # caso jogue um valor que não está entre o primeiro e o último indice da lista OU caso a lista já esteja com 10 jogadores (significa que está cheia), ele retorna false e sai do método, se não, retorna true
        if posicao_desejada_lista > len(self.__lista_jogadores) or posicao_desejada_lista < 0 or len(self.__lista_jogadores) >= 10:
            return False
        return True
     
    # 5 passo, ao final, o ranking deve ser ordenado em ordem alfabética (tentar passar essa lógica para o index)   
    def ordena_ranking(self)->None:
        # sort vai ordenar em ordem alfabética a lista, fazendo isso, 
        # não posso dar um return em algo como: self.__lista_jogadores.sort() pois vai retornar null, então devo ordenar a lista primeiro e então retorna-la
        self.__lista_jogadores.sort()
        print(f"=== Ranking ordenado ===")
        contador = 0
        while contador < len(self.__lista_jogadores):
            print(f"{contador} - {self.__lista_jogadores[contador]}")
            contador += 1
    
    # 6 passo, informar quantas vezes um determinando nome aparece na lista (feito utilizando função count)
    def contagem_nomes(self, nome_jogador: str)->None:
        quantidade_aparicoes_nome = self.__lista_jogadores.count(nome_jogador)
        print(f"O nome do jogador(a): {nome_jogador} aparece: {quantidade_aparicoes_nome} vezes no ranking.")
        self.mostrar_lista()
    
    # 7 passo, a lista deve ser exibida após cada operação, então defini um método para ser executado a cada operação da lista
    def mostrar_lista(self)->None:
        contador = 0
        print("=== Ranking atualizado ===")
        while contador < len(self.__lista_jogadores):
            print(f"{contador} - {self.__lista_jogadores[contador]}")
            contador += 1

# criando jogadores 
jogador_um = Jogador("Ana")
jogador_dois = Jogador("Bruno")
jogador_tres = Jogador("Carlos")

# criando ranking
ranking = Ranking()

# adicionando jogadores ao ranking
ranking.add_jogadores_final_lista(jogador_um.get_nome())
ranking.add_jogadores_final_lista(jogador_dois.get_nome())
ranking.add_jogadores_final_lista(jogador_tres.get_nome())

jogador_quatro = Jogador("Zelda")
# inserir o jogador Zelda na posição 1
ranking.add_jogadores_posicao_especifica(1, jogador_quatro.get_nome())
# remover o jogador que estiver na posição 2
ranking.remover_jogador_pelo_indice(2)
# ordenando o ranking
ranking.ordena_ranking()
# contando quantas vezes o nome ana aparece
ranking.contagem_nomes(jogador_um.get_nome())