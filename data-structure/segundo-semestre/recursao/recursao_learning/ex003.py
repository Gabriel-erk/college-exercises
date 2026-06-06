def contagem_recursiva(lista):
    if lista == []:
        return 0
    return 1 + contagem_recursiva(lista[1:])

valores = [10, 20, 30, 40]
# primeira chamada == (0 + 1) == 1 + contagem_recursiva[20,30,40] == indice 1,2,3
# segunda chamada == (1 + 1) == 2 + contagem_recursiva[30,40] == indice 1,2 (pois devido ao fatiamento, eu estou criando uma NOVA lista sem contar o primeiro elemento (indice 0 da lista que fatiei))
# terceira chamada == (1 + 1 + 1) == 3 + contagem_recrusiva[40] == indice 1
# quarta chamada == (1 + 1 + 1 + 1) == 4 + contagem_recursiva[] == aqui eu apenas tenho o indice 0, mas ele não está visível pra mim pois no fatiamento estou pedindo a partir do indice 1
# quinta chamada == cai no caso base, retorna 0 e encerra a sequência de chamadas

print(contagem_recursiva(valores))