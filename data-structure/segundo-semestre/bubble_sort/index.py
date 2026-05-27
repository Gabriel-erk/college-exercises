def bubble_sort(lista):
    tamanho_lista = len(lista) # guarda o tamanho da lista, supunhetando que é uma lista de 5 valores, aqui o valor será 5
    
    # controla quantas passagens jã foram feitas
    passagem = 0
    
    # enquanto ainda existirem passagens nececessárias (enquanto não repetiu para todo mundo) (tamanho_lista - 1 pois não quero ir até 5, já que na lista imaginária são apenas 5 elementos de 0 ao indice 4)
    while passagem < tamanho_lista - 1:
        print(f"\n=========== PASSAGEM {passagem + 1} ===========")
        
        # indice usado para percorrer a lista
        i = 0
        while i < tamanho_lista - 1:
            print(f"Comparando {lista[i]} e {lista[i+1]}")
            
            # se o elemento atual for maior que o próximo, eles estão na posição errada, logo, são invertidos
            if lista[i] > lista[i + 1]:
                # aux == salvar o atual pois será realizada uma troca com o próximo, por isso o aux está recebendo o valor atual == lista[i]
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                print("Troca realizada")
            else:
                print("Nenhuma troca necessária")
        
            # mostra o estado atual da lista
            print(f"Lista atual: {lista}")
            
            # avança para próximo
            i += 1
        # finaliza cada uma das passagens
        passagem += 1
    return lista

def bubble_sort_resumido(lista):
    tamanho_lista = len(lista)
    
    passagem = 0
    
    while passagem < tamanho_lista - 1:
        
        i = 0
        while i < tamanho_lista - 1:
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
            i += 1
        passagem += 1
    return lista

# melhor para listas pequenas (100000 por ex demoraria mto esse bubble)
numeros = [8,3, 7, 1,5,2]
print(f"Lista original: {numeros}")
resultado = bubble_sort_resumido(numeros)
print(f"Lista ordenada: {resultado}")
