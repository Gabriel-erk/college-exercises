def soma_recursiva(lista):
    if lista == []: 
        return 0

    return lista[0] + soma_recursiva(lista[1:])


valores = [35.90, 12.50, 8.00, 20.00]

resultado = soma_recursiva(valores)

print(resultado)