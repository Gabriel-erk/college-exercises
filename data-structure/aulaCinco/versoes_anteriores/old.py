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
    
class Playlist:
    lista_musicas = []
    
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
    
    def calcula_tempo_playlist(self)->int:        
        contador = 0
        soma_tempo_playlist = 0
        while contador < len(self.lista_musicas):
            soma_tempo_playlist += self.lista_musicas[contador].get_duracao_em_minutos()
            contador += 1
        return soma_tempo_playlist
    
    def tempo_playlist_por_genero(self)->None:
        lista_generos = []
        contador = 0
        # pegando todos os genêros (incluindo os repetidos)
        while contador < len(self.lista_musicas):
            lista_generos[contador] = self.lista_musicas[contador].get_genero_musical()
            contador += 1
        # loop para remover genêros repetidos
        segundo_contador = 0
        while segundo_contador < len(lista_generos):
            i = 0
            while i < len(lista_generos):
                if lista_generos[segundo_contador] == lista_generos[i]:
                    # removendo pelo indice o genero que tiver na posição i pois ele será um repetido
                    lista_generos.pop(i) 
                    i += 1 
            segundo_contador += 1
        # realizando a soma por genero
        soma_tempo_playlist_por_genero = 0
        terceiro_contador = 0
        # preciso percorrer todas as músicas
        while terceiro_contador < len(self.lista_musicas):
            i_genero = 0
            # agora preciso que todas as músicas passem por todos os generos
            while i_genero < len(lista_generos):
                # se o genero da musica atual for igual ao genero atual, 
                if self.lista_musicas[i_genero].get_genero_musical() == lista_generos[terceiro_contador]:
                    soma_tempo_playlist_por_genero += self.lista_musicas[i_genero].get_duracao_em_minutos()
            terceiro_contador += 1
        return soma_tempo_playlist_por_genero