def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1 # último indice da lista == fim da lista
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if alvo == lista[meio]:
            return lista[meio]
        # se meu valor procurado é menor que o valor que está no meio da lista (e eu sei que toda busca binária é feita quando os valores estão ORDENADOS (10, 20, 30....) sei que os indices MAIORES que o indice dentro da váriavel meio vão me entregar apenas valores MAIORES AINDA que o meio atual quando comparados ao meu valor alvo, logo, por isso, vou olhar apenas para o lado esquerdo agora, que possui valores menores que o meio e provavelmente é onde deve estar o meu alvo)
        if alvo < lista[meio]:
            # meu inicio permanece normal, mudo apenas o valor de fim, não coloco = meio pois eu já sei que ele NÃO É IGUAL ao meio, pois se fosse, tinha caido no PRIMEIRO if desse método, logo, não preciso olhar pra ele de novo
            fim = meio - 1
         
        if alvo > lista[meio]:
            # se o alvo é maior que o valor que está no meio, logo, ele está a parte direita da lista (considerando sempre que, minha lista é sempre ordenada), sei que o meio não possui o valor procurado, pois se tivesse caia no primeiro if do método (que vê se o valor do meio é igual ao valor procurado) por isso meio + 1 (para que eu não olhe para o mesmo valor twice)
            inicio = meio + 1
            
    return -1

lista = [10, 20, 30, 40, 50, 60, 70]

valor_procurado = busca_binaria(lista, 10)

print(valor_procurado)