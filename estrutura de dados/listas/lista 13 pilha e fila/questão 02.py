def menu():
    print("="*15)
    print("Cremilda chantilly")
    print("="*15)
    print("1 - visualizar lista ")
    print("2 - adicionar paciente")
    print("3 - Remover paciente ")
    print("4 - Sair")
    print("="*15)

def mostrar_fila(fila):
    if fila:
        print("Fila de pacientes:")
        for paciente in fila:
            print(f"- {paciente}")
    else:
        print("A fila está vazia.")


def adicionar_paciente(nome, fila):
    fila.append(nome)
    return fila
   
def remover_paciente(fila):
    return fila.pop(0)

#progama principal


menu()

fila_paciente = []
esc = int(input())


while esc != 4:
    if esc < 1 or esc > 4:
        print ("Escolha outra opção")
    menu()

    esc = int(input())

    if esc == 1:
        mostrar_fila(fila_paciente)


    elif esc == 2:
       
        nome_paciente = input()
        print(adicionar_paciente(nome_paciente, fila_paciente))
       
    elif esc == 3:
        if len(fila_paciente) <= 0:
            print("Não há pacientes")  
        print(remover_paciente(fila_paciente))



