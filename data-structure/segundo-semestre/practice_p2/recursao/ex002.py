def contagem_regressiva(n):
    if n == 0:
        print(n)
        print("Iniciando transmissão!")
        return n
    print(n)
    return contagem_regressiva(n - 1)

contagem_regressiva(5)

