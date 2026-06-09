def bubble_sort(lista):
    passagem = 0
    while passagem < len(lista) - 1:
        i = 0
        while i < len(lista) - 1:
            if lista[i].codigo > lista[i + 1].codigo:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
            i += 1
        passagem += 1
    return lista

def busca_binaria(lista, alvo):
    inicio = 0 
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if alvo == lista[meio].codigo:
            return lista[meio]
        
        if alvo < lista[meio].codigo:
            fim = meio - 1
        
        if alvo > lista[meio].codigo:
            inicio = meio + 1
    return -1

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

produto1 = Produto(305, "Teclado", 120.00)
produto2 = Produto(101, "Mouse", 59.90)
produto3 = Produto(450, "Monitor", 899.00)
produto4 = Produto(220, "Webcam", 199.90)
produto5 = Produto(150, "Headset", 249.90)

produtos = [produto1, produto2, produto3, produto4, produto5]

produtos = bubble_sort(produtos)

i = 0 
print("Produtos ordenados por código:")
while i < len(produtos):
    print(f"{produtos[i].codigo} - {produtos[i].nome} - R$ {produtos[i].preco}")
    i += 1

codigo_buscado = 220

produto = busca_binaria(produtos, codigo_buscado)

print("")

if produto != -1:
    print("Produto encontrado:")

    print(f"Código: {produto.codigo}")       
    print(f"Nome: {produto.nome}")       
    print(f"Preço: R$ {produto.preco}")
else:
    print("Produto não encontrado.")       

        