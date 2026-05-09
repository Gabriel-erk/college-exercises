class Musica:
    def __init__(self, nome_musica: str, nome_artista: str, duracao_em_minutos: int, genero_musical: str):
        self.__nome_musica = nome_musica
        self.__nome_artista = nome_artista
        self.__duracao_em_minutos = duracao_em_minutos
        self.__genero_musical = genero_musical
    
    def get_nome_musica(self)->str:
        return self.__nome_musica
    
    def get_nome_artista(self)->str:
        return self.__nome_artista
    
    def get_duracao_em_minutos(self)->int:
        return self.__duracao_em_minutos
    
    def get_genero_musical(self)->str:
        return self.__genero_musical
    
class Genero:
    generos = []
    
    def __init__(self, nome_genero: str, minutagem: int):
        self.nome_genero = nome_genero
        self.minutagem = minutagem

class Playlist:
    lista_musicas = []
    lista_generos = []
    
    def __init__(self, nome_playlist: str):
        self.__nome_playlist = nome_playlist
    
    def get_nome_playlist(self)->str:
        return self.__nome_playlist
    
    def add_musica(self, musica: Musica)->str:
        self.lista_musicas.append(musica)
        return f"Música: {musica.get_nome_musica()} foi adicionada a playlist: {self.get_nome_playlist()}."
    
    def remover_musica(self, musica: Musica)->str:
        contador = 0
        while contador < len(self.lista_musicas):
            if self.lista_musicas[contador].get_nome_musica() == musica.get_nome_musica():
                # pop remove pelo contador
                self.lista_musicas.pop(contador)
                return f"Música: {musica.get_nome_musica()} foi removida da playlist: {self.get_nome_playlist()}."
            else:
                contador += 1
        return f"Música: {musica.get_nome_musica()} não foi encontrada na playlist: {self.get_nome_playlist()}."
    
    # declarando que o método não retorna nada (em python = None)
    def listar_musicas(self)->None:
        contador = 0
        print(f"--- Playlist: {self.get_nome_playlist()} ---")
        while contador < len(self.lista_musicas):
            print(f"Música 00{contador} - {self.lista_musicas[contador].get_nome_musica()}")
            contador += 1
    
    def calcula_tempo_playlist(self)->str:        
        contador = 0
        soma_tempo_playlist = 0
        while contador < len(self.lista_musicas):
            soma_tempo_playlist += self.lista_musicas[contador].get_duracao_em_minutos()
            contador += 1
        return f"A playlist: {self.get_nome_playlist()} tem {soma_tempo_playlist} minutos de duracao."
    
    # objetivo com este método é guardar o nome do genero e a sua minutagem, de forma que, caso uma nova música seja instanciada, eu passe o genero para cá e inicialize uma lista que guardará os genêros, a partir dele, eu realize a conta de forma automática onde, caso exista um genêro na lista com o nome da nova música passada, a minutagem seja acrescentada, se não existir um genêro com aquele nome, crie um objeto do tipo genero passando aquele nome, e somando com a minutagem
    # passo a passo
    # 1 - receber a música por parâmetro e verificar se o genero que ela possui já existe na minha lista (caso a lista esteja vazia, aquele é o primeiro) - (após o primeiro percorro a lista inteira, se aquele genero não está la, crio e adiciono a lista)
    def create_genero(self, musica: Musica):
        # se está nulo, está vazio e inicializo ela com o genero da primeira música passada
        contador = 0
        if self.lista_generos == None:
            genero = Genero(musica.get_genero_musical(), musica.get_duracao_em_minutos())
            self.lista_generos.append(genero)
        else:
            while contador < len(self.lista_generos):
                if musica.get_genero_musical() == self.lista_generos[contador]:
                    self.lista_generos[contador]. += 
                    
    def tempo_por_genero(self)->None:
        # pegar o genero da primeira musica, somar o tempo da musica a váriavel que será a responsavel por exibir os o tempo total de cada genero, procurar o mesmo genero na lista, se encontrar, soma, se não, exibe o tempo daquel genero e passa para o próximo genero
        contador = 0
        soma_tempo_por_genero = 0
        # primeiro percorrer todas as músicas
        while contador < len(self.lista_musicas):
            i = 0
            lista_generos_contados = []
            # caso a condição do if fosse verdadeira, ele nunca teria acesso ao primeiro valor, apenas ao do lado direito da comparação (self.lista_musicas[i]), somaria todos os generos iguais ao que esta sendo comparado mas nunca o que esta comparando
            soma_tempo_por_genero = self.lista_musicas[contador].get_duracao_em_minutos()
            # pegar o genero de cada musica e comparar com todos da lista, começando da posição 0
            while i < len(self.lista_musicas):
                if self.lista_musicas[contador].get_genero_musical() == self.lista_musicas[i].get_genero_musical():
                    j = 0
                    while j < len(lista_generos_contados):
                        if self.lista_musicas[contador].get_genero_musical() == lista_generos_contados[j]:
                            j += 1
                        else:
                            lista_generos_contados.append(self.lista_musicas[contador])
                            soma_tempo_por_genero += self.lista_musicas[i].get_duracao_em_minutos()
                i += 1
            # imprimo a soma do genero atual
            print(f"Genêro: {self.lista_musicas[contador].get_genero_musical()} - Tempo total: {soma_tempo_por_genero}")
            # zero a variavel responsavel pela soma de cada genero para que o proximo valor que eu va somar seja de outro genero já que ela "já teve seu uso" para o genero atual
            soma_tempo_por_genero = 0
            contador += 1 

musica_um = Musica("Let it go", "Elsa do frozen", 5, "Infantil")
musica_dois = Musica("Drama", "Roy Woods", 5, "R&B")
musica_tres = Musica("Essa noite eu bebi amor", "Dfideliz", 4, "R&B")
musica_quatro = Musica("Enter Sadman", "Metalica", 6, "Rock")
playlist_um = Playlist("Playlist do g.a")

print("=== Adicionando músicas ===")
print(playlist_um.add_musica(musica_um))
print(playlist_um.add_musica(musica_dois))
print(playlist_um.add_musica(musica_tres))
print(playlist_um.add_musica(musica_quatro))

print("=== Listando músicas após adição ===")
print(playlist_um.listar_musicas())

print("=== Removendo música ===")
print(playlist_um.remover_musica(musica_um))
# print(playlist_um.remover_musica(musica_um))

print("=== Calculando tempo da playlist ===")
print(playlist_um.calcula_tempo_playlist())

print("=== Tempo para cada genêro musical ===")
print(playlist_um.tempo_por_genero())