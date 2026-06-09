class Produto:
    def __init__(self,codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

produto1 = Produto(101, "Arroz", 25.90)
produto2 = Produto(205, "Feijão", 8.50)
produto3 = Produto(150, "Macarrão", 5.75)

produtos = [produto1, produto2, produto3]

codigo_buscado = 205

i = 0
produto_encontrado = {}
while i < len(produtos):
    if produtos[i].codigo == codigo_buscado:
        produto_encontrado = produtos[i]
        
        print("Produto encontrado:")
        print(f"Código: {produto_encontrado.codigo}")
        print(f"Nome: {produto_encontrado.nome}")
        print(f"Preço: R$ {produto_encontrado.preco}")
        
        break
    i += 1

if produto_encontrado == {}:
    print("Produto não encontrado.")
    
