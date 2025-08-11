def menu():
    print("="*15)
    print("tuconaldo")
    print("="*15)
    print("1 - visualizar pilha ")
    print("2 - adicionar peça")
    print("3 - Remover peça")
    print("4 - Sair")
    print("="*15)

def adicionar_pilha(pilha, peca):
    pilha.append(peca)
    return pilha
def remover_pilha(pilha):
    pilha.pop(0)
    return pilha 

def mostrar_pilha(pilha):
    if len(pilha) <= 0:
          print("Não ha pecas")
    for pecas in pilha:
        print(pecas)
      


                #progama principal#

pilha_pecas = []

menu()
escolha = int(input())

while escolha > 1 or escolha <= 4:
    if escolha == 1:
        mostrar_pilha(pilha_pecas)
    if escolha == 2:
        pass
    if escolha == 3:
        pass
    if escolha == 4:
        pass
