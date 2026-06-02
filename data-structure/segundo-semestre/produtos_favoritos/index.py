class Produto:
    #  já vai atuar como cadasro de produto
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        
    def show(self):
        print(f"{self.nome} - R$ {self.preco}")

class Favoritos:
    def __init__(self):
        self.__produtos = []

    def add_favorito(self, produto):
        self.__produtos.append(produto)
    
    def show(self):
        i = 0
        # visualizar produtos cadastrados na lista de favoritos
        while i < len(self.__produtos):
            self.__produtos[i].show()
            i += 1
    
    def bubble_sort(self, metodo_ordenacao):
        tamanho = len(self.__produtos)
        passagem = 0
        
        if metodo_ordenacao == "crescente":
            while passagem < tamanho - 1:
                i = 0
                while i < tamanho - 1:
                    if self.__produtos[i].preco > self.__produtos[i + 1].preco:
                        aux = self.__produtos[i]
                        self.__produtos[i] = self.__produtos[i + 1]
                        self.__produtos[i + 1] = aux
                    i += 1
                passagem += 1 
        elif metodo_ordenacao == "decrescente":
            while passagem < tamanho - 1:
                i = 0
                while i < tamanho - 1:
                    if self.__produtos[i].preco < self.__produtos[i + 1].preco:
                        aux = self.__produtos[i]
                        self.__produtos[i] = self.__produtos[i + 1]
                        self.__produtos[i + 1] =  aux
                    i += 1
                passagem += 1

produto_um = Produto("Notebook", 3500, "Tecnologia")
produto_dois = Produto("Mouse", 120, "Tecnologia")
produto_tres = Produto("Teclado", 250, "Tecnologia")
produto_quatro = Produto("Monitor", 900, "Tecnologia")

lista_favoritos = Favoritos()

lista_favoritos.add_favorito(produto_um)
lista_favoritos.add_favorito(produto_dois)
lista_favoritos.add_favorito(produto_tres)
lista_favoritos.add_favorito(produto_quatro)

lista_favoritos.bubble_sort("crescente")
print("Saída esperada (ordem crescente):")
lista_favoritos.show()

print("")

lista_favoritos.bubble_sort("decrescente")
print("Saída esperada (ordem decrescente):")
lista_favoritos.show()

print("")

print("=== Respostas 'reflexão' ===")
print("1 - Organização da lógica, facilitando a ordenação e compreendimento do sistema.")
print("2 - Pois em uma lista muito grande seria necessárioa uma grande quantidade de trocas de valores, gerando consequentemente um grande numero de comparações entre valores o que poderia exigir um tempo alto do sistema para retornar algum valor.")
print("3 - Atributo do objeto na comparação foi o: 'preco'")
