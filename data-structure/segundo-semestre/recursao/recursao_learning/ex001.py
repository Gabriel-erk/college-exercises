def soma_recursiva(lista): # método recursivo que recebe uma lista de parâmetro
    if lista == []:  # caso, base, para que não repita para sempre/para que não entre em um loop ifinito de chamadas da mesma func, eu defino um condićão para ela parar, nesse caso, quero que pare (ou seja, quero que retorne ZERO e não outra chamada da func) quando a lista que recebermos por parâmetro for vazia (pois não haverá mais numeros para somar == objetivo da func)
        return 0

    return lista[0] + soma_recursiva(lista[1:])


valores = [35.90, 12.50, 8.00, 20.00]

resultado = soma_recursiva(valores)

print(resultado)