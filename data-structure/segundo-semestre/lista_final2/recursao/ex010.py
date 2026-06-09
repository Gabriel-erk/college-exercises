def contagem_recursiva(numero):
    print(numero)
    if numero == 0:
        print("Iniciando transmissão!")
        return numero
    return contagem_recursiva(numero - 1)

contagem_recursiva(10)
