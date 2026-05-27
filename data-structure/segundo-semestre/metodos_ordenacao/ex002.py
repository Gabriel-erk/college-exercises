def selection_sort_decrescente(lista)->list:
    tamanho = len(lista)
    atual = 0
    
    while atual < tamanho - 1:
        indice_menor = atual
        i = atual + 1
        
        while i < tamanho:     
            if lista[i] > lista[indice_menor]:
                indice_menor = i
            i += 1
        
        if indice_menor != atual:
            aux = lista[atual]
            lista[atual] = lista[indice_menor]
            lista[indice_menor] = aux
        atual += 1
    return lista

lista_valores_produtos = [120, 450, 200, 980, 300]
print("Entrada sugerida:", end="")
print(lista_valores_produtos)

print("")

lista_valores_produtos_ordenado = selection_sort_decrescente(lista_valores_produtos)
print("Saída esperada:", end=" ")
print(lista_valores_produtos_ordenado)