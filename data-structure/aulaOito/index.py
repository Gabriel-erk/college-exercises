class ItemEncontrado:
    def __init__(self, nome: str, comodo: str, nivel_perigo: str):
        self.__nome = nome
        self.__comodo = comodo
        self.__nivel_perigo = nivel_perigo
    
    def get_nome(self)->str:
        return self.__nome

    def get_comodo(self)->str:
        return self.__comodo

    def get_nivel_perigo(self)->str:
        return self.__nivel_perigo
    
objetos_encontrados = {}
while(True):
    print("=== Menu de opções ===")
    print("1 - Cadastrar objeto (limite de 3)")
    print("2 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        while len(objetos_encontrados) < 3:
            nome_objeto_encontrado = input("Digite o nome do objeto: ")
            comodo_objeto_encontrado = input("Digite o comôdo onde o objeto foi encontrado: ")
            nivel_perigo_objeto_encontrado = input("Digite o nível de perigo do objeto encontrado (baixo, medio e alto): ")
            
            if nome_objeto_encontrado not in objetos_encontrados:
                objeto_encontrado = ItemEncontrado(nome_objeto_encontrado, comodo_objeto_encontrado, nivel_perigo_objeto_encontrado)
                
                objetos_encontrados[objeto_encontrado.get_nome()] = {
                    "comodo": objeto_encontrado.get_comodo(),
                    "perigo": objeto_encontrado.get_nivel_perigo() 
                }
                print(f"Objeto: '{nome_objeto_encontrado}' adicionado ao inventário!") 
            else:
                print("Objeto já está no inventário, não foi possível adicionar.")
            print("")
        print("Inventário foi preenchido.")
    else:
        if len(objetos_encontrados) > 0:
            print("Objetos encontrados na casa:")
            print("")
            objetos_perigosos_encontrados = 0
            for objeto_encontrado in objetos_encontrados:
                print(f"{objeto_encontrado} - Encontrado(a) no {objetos_encontrados[objeto_encontrado]["comodo"]} - Perigo: {objetos_encontrados[objeto_encontrado]["perigo"]}")
                if objetos_encontrados[objeto_encontrado]["perigo"] == "alto":
                    objetos_perigosos_encontrados += 1
            print("")
            print(f"Total de objetos perigosos: {objetos_perigosos_encontrados}")
            print("")
            print("Obrigado por utilizar o sistema!")
        else:
            print("Nenhum Objeto foi encontrado na casa.")
        break