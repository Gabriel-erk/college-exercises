def soma_recursiva(valores):
    if valores == []:
        return 0
    
    return valores[0] + soma_recursiva(valores[1:])

valores = [35.90, 12.50, 8.00, 20.00]
# primeira iteracao == valores[0] (35.90) + soma_recursiva(valores[1:]) == soma_recursiva(12.50, 8.00, 20.00) 
# fatiamento realizado a partir do indice 1 (pegou a lista apenas a partir do indice um e passou uma nova lista com os valores a partir do indice 1 (12.50, 8.00, 20.00) para o método soma_recursiva fazendo com que: indice 0 agora seja o 12.50)
# segunda iteracao == valores[0] (12.50) + soma_recursiva(valores[1:] == soma_recursiva(8.00, 20.00)) 
# terceira iteracao == valores[0] (8.00) + soma_recursiva(valores[1:]) == soma_recursiva(20.00) 
# quarta iteracao == valores[0] (20.00) + soma_recursiva(valores[1:]) == soma_recursiva() (nada pois a partir do indice 1, não temos mais nada) 
# quinta iteracao == cai no caso base, pois como realizamos um fatiamento na quarta iteracao, a lista ficou vazia, logo, return 0 , onde comećamos a somar, de baixo pra cima, logo: (resolućão abaix)

#RESOLUĆÃO DESSE CARALHO DE RECURSÃO (soma realizada nessa ordem, de ponta cabeća mesmo)
# 1 passo - resultado quinta iteracao + resultado quarta iteracao == 0 + 20.00
# 2 passo - resultado anterior (soma do resultado quinta iteracao com resultado quarta iteracao) + resultado quarta iteracao == 20 + 8
# 3 passo - resultado anterior (resultado do 1 passo + resultado da quarta iteracao) + resultado terceira iteracao == 28 + 12.5
# 4 passo - resultado anterior (28 + 12.5) + resultado da segunda iteracao == 40.5
# 5 passo - resultado anterior (40.5) + resultado da primeira iteracao == 35.9 + 40.5 == 76.4

print(f"Total da compra: {soma_recursiva(valores)}")