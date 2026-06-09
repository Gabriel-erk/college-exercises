class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome

def busca_binaria(lista, valor_buscado):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if valor_buscado == lista[meio].ra:
            return lista[meio]
        
        if valor_buscado < lista[meio].ra:
            fim = meio - 1
        
        if valor_buscado > lista[meio].ra:
            inicio = meio + 1
    return -1    
        
    

aluno1 = Aluno(2024001, "Ana")
aluno2 = Aluno(2024002, "Bruno")
aluno3 = Aluno(2024003, "Carla")
aluno4 = Aluno(2024004, "Daniel")
aluno5 = Aluno(2024005, "Eduarda")
alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
ra_buscado = 2024004

teste = busca_binaria(alunos, ra_buscado)
print(teste.ra)

