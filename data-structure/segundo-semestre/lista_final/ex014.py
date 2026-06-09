class Arquivo:
    def __init__(self, nome, tamanho_mb):
        self.nome = nome
        self.tamanho_mb = tamanho_mb


class Pasta:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)


def calcular_tamanho(pasta):
    total = 0

    for item in pasta.itens:

        if type(item) == Arquivo:
            total += item.tamanho_mb

        elif type(item) == Pasta:
            total += calcular_tamanho(item)

    return total


arquivo1 = Arquivo("main.py", 2)
arquivo2 = Arquivo("README.md", 1)

imagem1 = Arquivo("logo.png", 5)
imagem2 = Arquivo("banner.png", 8)

documento1 = Arquivo("contrato.pdf", 12)

nota1 = Arquivo("anotacoes.txt", 3)

pasta_imagens = Pasta("imagens")
pasta_imagens.adicionar(imagem1)
pasta_imagens.adicionar(imagem2)

pasta_notas = Pasta("notas")
pasta_notas.adicionar(nota1)

pasta_documentos = Pasta("documentos")
pasta_documentos.adicionar(documento1)
pasta_documentos.adicionar(pasta_notas)

pasta_projeto = Pasta("Projeto")
pasta_projeto.adicionar(arquivo1)
pasta_projeto.adicionar(arquivo2)
pasta_projeto.adicionar(pasta_imagens)
pasta_projeto.adicionar(pasta_documentos)

print(
    f"Tamanho total da pasta {pasta_projeto.nome}: "
    f"{calcular_tamanho(pasta_projeto)} MB"
)