def bubble_sort_decrescente(lista):
    tamanho_lista = len(lista)
    
    passagem = 0
    
    while passagem < tamanho_lista - 1:
        
        i = 0
        while i < tamanho_lista - 1:
            if lista[i] < lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
            i += 1
        passagem += 1
    return lista


print("Entrada sugerida:", end=" ")
lista = [15, 2, 30, 9, 1]
print(lista)

lista_ordenada = bubble_sort_decrescente(lista)
print("Saída esperada:", end=" ")
print(lista_ordenada)                
