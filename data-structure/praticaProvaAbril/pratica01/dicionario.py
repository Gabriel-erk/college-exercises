# informações a guardar no dicionário:
# nome
# comodo onde foi encontrado
# nivel de perigo (baixo, medio ou alto)

# dicionário vazio
objetos_encontrados = {}
opcao = 99

while opcao != 0:

    print("0 - Sair")
    if len(objetos_encontrados) < 3:
        print("1 - Cadastrar objeto")
    print("2 - Ver todos")
    opcao = int(input("Digite uma opção:"))
    
    if opcao == 0:
        print("Inventário encerrado.")
        break
    elif opcao == 1:
        while len(objetos_encontrados) < 3:
            nome_objeto_encontrado = input("Digite o nome do objeto encontrado: ")
            comodo_objeto_encontrado = input("Digite o cômodo do objeto encontrado: ")
            nivel_perigo_objeto_encontrado = input("Digite o nível de perigo do objeto encontrado: ")
        
            objetos_encontrados[nome_objeto_encontrado] = {
                "comodo": comodo_objeto_encontrado,
                "nivel_perigo": nivel_perigo_objeto_encontrado
            }
            
            print()
    elif opcao == 2:
        print("Objetos encontrados na casa:")
        objetos_perigosos_encontrados = 0
        for objeto_encontrado in objetos_encontrados:
            if objetos_encontrados[objeto_encontrado]["nivel_perigo"] == "alto":
                objetos_perigosos_encontrados += 1
            print(f"{objeto_encontrado} - Econtrado(a) no {objetos_encontrados[objeto_encontrado]["comodo"]} - Perigo: {objetos_encontrados[objeto_encontrado]["nivel_perigo"]}")
        print()
        print(f"Total de objetos perigosos: {objetos_perigosos_encontrados}")
    else: 
        print("Opção Inválida.")
    
    