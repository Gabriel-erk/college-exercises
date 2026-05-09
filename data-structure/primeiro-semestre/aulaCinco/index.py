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
                self.lista_musicas.remove(self.lista_musicas[contador])
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
                    
    def tempo_por_genero(self)->None:
        lista_generos = []
        soma_minutos_genero = 0
        # adicionando todos os generos na lista
        for musica in self.lista_musicas:
            if musica.get_genero_musical() not in lista_generos:
                lista_generos.append(musica.get_genero_musical())
        
        for genero in lista_generos:
            for musica in self.lista_musicas:
                if musica.get_genero_musical() == genero:
                    soma_minutos_genero += musica.get_duracao_em_minutos()
            print(f"Genêro: {genero} - Minutos: {soma_minutos_genero}")
            soma_minutos_genero = 0

musica_um = Musica("Let it go", "Elsa do frozen", 5, "Infantil")
musica_dois = Musica("Drama", "Roy Woods", 5, "R&B")
musica_tres = Musica("Essa noite eu bebi amor", "Dfideliz", 4, "R&B")
musica_quatro = Musica("Overtime", "Bryson Tiller", 5, "R&B")
musica_cinco = Musica("Enter Sadman", "Metalica", 6, "Rock")
musica_seis = Musica("Nothing else matter", "Metalica", 6, "Rock")
playlist_um = Playlist("Playlist do g.a")

print("=== Adicionando músicas ===")
print(playlist_um.add_musica(musica_um))
print(playlist_um.add_musica(musica_dois))
print(playlist_um.add_musica(musica_tres))
print(playlist_um.add_musica(musica_quatro))
print(playlist_um.add_musica(musica_cinco))
print(playlist_um.add_musica(musica_seis))

print("=== Listando músicas após adição ===")
print(playlist_um.listar_musicas())

print("=== Removendo música ===")
print(playlist_um.remover_musica(musica_um))
# print(playlist_um.remover_musica(musica_um))

print("=== Calculando tempo da playlist ===")
print(playlist_um.calcula_tempo_playlist())

print("=== Tempo para cada genêro musical ===")
print(playlist_um.tempo_por_genero())
# print(playlist_um.tempo_por_genero(musica_dois))
# print(playlist_um.tempo_por_genero(musica_tres))
# print(playlist_um.tempo_por_genero(musica_quatro))