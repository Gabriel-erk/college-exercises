def bubble_sort(lista_palavras):
    tamanho_lista = len(lista_palavras)
    passagem = 0
    trocas_realizadas = []

    while passagem < tamanho_lista - 1:        
        i = 0
        while i < tamanho_lista - 1:
            if len(lista_palavras[i]) > len(lista_palavras[i + 1]):
                
                aux = lista_palavras[i]
                
                lista_palavras[i] = lista_palavras[i + 1]
                lista_palavras[i + 1] = aux
                trocas_realizadas.append(f"Troca entre: {lista_palavras[i]} e {lista_palavras[i + 1]}")
                # print(f"Troca entre: {lista_palavras[i]} e {lista_palavras[i + 1]}")
            i += 1
        passagem += 1
    print("Trocas realizadas:", end=" ")
    print(trocas_realizadas)
    return lista_palavras

lista_palavras = ["python", "ia", "estrutura", "web", "dados"]
print("Entrada sugerida:", end=" ")
print(lista_palavras)

print("")

lista_palavras = bubble_sort(lista_palavras)
print("Saída esperada:", end=" ")
print(lista_palavras)

print("")