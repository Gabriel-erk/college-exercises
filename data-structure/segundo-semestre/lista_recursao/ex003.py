def somar_lista(lista):
    if len(lista) == 0:
        return 0

    return lista[0] + somar_lista(lista[1:])


numeros = [10, 20, 30, 40]

print(somar_lista(numeros))