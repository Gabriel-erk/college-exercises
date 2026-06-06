def contagem_recursiva(numero):
    print(numero)
    if numero == 0:
        print("Iniciando transmissão!")
        return numero
    return contagem_recursiva(numero - 1)

# primeira chamada == contagem_recursiva(9) pois: contagem_recursiva(numero (aqui vale 10, mas reduzi 1, logo, passei o valor 9 para a fun contagem_recursiva) - 1)
# segunda chamada == contagem_recursiva(8)  pois: contagem_recursiva(numero (aqui vale 9, mas reduzi 1, logo, passei o valor 8 para a fun contagem_recursiva) - 1)
# terceira chamada == contagem_recursiva(7)  pois: contagem_recursiva(numero (aqui vale 8, mas reduzi 1, logo, passei o valor 7 para a fun contagem_recursiva) - 1)
# quarta chamada ==  pois: contagem_recursiva(numero (aqui vale 7, mas reduzi 1, logo, passei o valor 6 para a fun contagem_recursiva) - 1)
# e por ai vai até chegar no caso base, onde: se numero for igual a 0, retorno ele mesmo
contagem_recursiva(10)
