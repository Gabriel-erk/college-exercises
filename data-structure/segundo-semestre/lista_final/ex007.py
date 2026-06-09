def bubble_sort(numbers):
    passagem = 0
    quantidade_trocas = 0
    while passagem < len(numbers) - 1:
        i = 0
        while i < len(numbers) - 1:
            if numbers[i] > numbers[i + 1]:
                aux = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = aux
                
                quantidade_trocas += 1
            i += 1
        passagem += 1
    print(f"Notas ordenadas: {numbers}")
    print(f"Quantidade de trocas: {quantidade_trocas}")

notas = [7.5, 5.0, 9.0, 6.5, 8.0]

bubble_sort(notas)


