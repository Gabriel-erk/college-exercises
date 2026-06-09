def bubble_sort(lista):
    passagem = 0
    qntd_trocas = 0
    while passagem < len(lista) - 1:
        i = 0
        while i < len(lista) - 1:
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                qntd_trocas += 1
            i += 1
        passagem += 1
    print(f"Valores ordenados: {lista}")
    print(f"Quantidade de trocas: {qntd_trocas}")

notas = [7.5, 5.0, 9.0, 6.5, 8.0]

bubble_sort(notas)

