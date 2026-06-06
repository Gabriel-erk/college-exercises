def soma_pares(lista):
    if lista == []:
        return 0
    if lista[-1 + 1] % 2 == 0 and lista[1] % 2 == 0:
        return (lista[-1 + 1] + lista[1]) + soma_pares(lista[1:])
    return soma_pares(lista[1:])

valores = [1, 2, 3, 4, 5, 6]

print(soma_pares(valores))
    