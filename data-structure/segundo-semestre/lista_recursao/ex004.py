def contagem_regressiva(n):
    print(n)

    if n == 0:
        print("Lançamento autorizado!")
        return

    contagem_regressiva(n - 1)


contagem_regressiva(5)