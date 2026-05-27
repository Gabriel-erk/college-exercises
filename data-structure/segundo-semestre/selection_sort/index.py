def selection_sort(lista)->list:
    # tamanho da lista (preciso saber quantos elementos tem)
    tamanho = len(lista)
    
    # indice da posiçâo atual da ordenaçâo (listas lineares sempre começadm iterações do 0, então aqui eu meio que forçõ isso, toda vez começa do 0)
    atual = 0
    
    while atual < tamanho - 1:
        print(f"\n========= PASSAGEM {atual + 1} =========")

        # assume inicialmente que o menor elemento é esse primeiro que ele recebeu
        # está na posição atual (0)
        indice_menor = atual
        
        # indice usado para procurar o menor valor (olhando o proximo)
        i = atual + 1
        
        # procrua o menor elemento no restante da lista
        
        while i < tamanho:
            print(f"Comparando {lista[i]} com {lista[indice_menor]}")
            
            # se encontrar um valor menor, atualize o indice do menor elemento
            if lista[i] < lista[indice_menor]:
                indice_menor = i
            
            # avança para o próximo elemento
            i += 1
        # ---------- while para achar o menor elemento em cada passagem, após encontrar o menor elemento, realiza a troca de posição
        if indice_menor != atual:
            print(f"Troca {lista[atual]} por {lista[indice_menor]}")
            aux = lista[atual]
            lista[atual] = lista[indice_menor]
            lista[indice_menor] = aux
        else:
            print("Nenhuma troca necessária")
        # mostra o estado atual da lista
        print("Lista atual", lista)
        atual += 1
    return lista

numeros = [8,3,7,1,5,2]
print(f"Lista original: {numeros}")
resultado = selection_sort(numeros)
print(f"Lista ordenada: {resultado}")