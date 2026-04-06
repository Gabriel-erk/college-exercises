class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# função 01
def mostrar_lista(head):
    contador = 0
    while head is not None:
        print(f"#{contador} - {head.data}")
        head = head.next
        contador += 1

# funçaõ 02
def inserir_fim(head, valor):
    # crio um novo objeto do tipo node com o valor passado para se adicionar no final
    novo_no = Node(valor)
    # se o head for nulo já no inicio do código, significa que já estou com o último valor, então, se o valor atual for None, eu já estou com o "ultimo", logo, ele receberá o valor do meu novo_no
    if head == None:
        head = novo_no
        # se caiu no else, o valor atual não é None, logo, tenho que procurar o último, então verifico se o PRÓXIMO é nulo, pois quando o PRÓXIMO for nulo, sei que o próximo é o último, logo, se o próximo for NONE, não vai atender a condição para "entrar no corpo do while", consequentemente, não entrará nele e executará a próxima linha: head.next = novo_no, definindo, através da referência, o valor passado como parâmetro como o valor final da nossa lista (porque não pode ser: while head is not None: faça algo aqui? - simples, pois tenho a instrução no corpo do while: head = head.next, o que faz com que uma hora o valor de "head" passe a ser None, ou seja, ele não é um objeto, o valor "None" não possui um "next" pois só possui um next objetos do tipo "Node", usando essa abordagem o valor de head vai ser None, consequentemente, não tem como eu atribuir um valor ao "next" a ele pois ele não possui um, "a mas se a instrução ao invés de head.next = novo_no fosse head = novo_no??", mesmo assim não funcionaria da forma esperada pois meio que "perderia o vínculo com a lista", já que meu head vale: "None" ele foi para um valor nulo, não para um valor vinculado aos outros valores da lista, ou seja, quando ele passou a valer none e parou de ter um next, ele perdeu o vinculo com a lista, ele até teria o valor do novo_no, mas não teria NENHUM vínculo com a lista )
    else:
        while head.next is not None:
            head = head.next
        head.next = novo_no    

# função 03
def buscar(head,valorProcurado)->bool:
    while head is not None:
        if head.data == valorProcurado:
            return True 
        head = head.next
    return False 

def contar_ocorrencias(head, valorProcurado)->str:
    contadorOcorrencias = 0
    while head is not None:
        if head.data == valorProcurado:
            contadorOcorrencias += 1
        head = head.next
    return f"O valor: {valorProcurado} aparece: {contadorOcorrencias}x na lista."
        
# instanciação
n1 = Node(5)
n2 = Node(10)
n3 = Node(5)
n4 = Node(20)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1

print("Etapa #1")
mostrar_lista(head)

print("-------------")
print("Etapa #2")
inserir_fim(head, 30)
mostrar_lista(head)

print("-------------")
print("Etapa #3")
if buscar(head, 10) == True:
    print(f"O valor: {10} está na lista.")
else:
    print(f"O valor: {10} não está na lista.")

print("-------------")
print("Etapa #4")
print(contar_ocorrencias(head, 5))

print("-------------")
print("Etapa #5")
mostrar_lista(head)