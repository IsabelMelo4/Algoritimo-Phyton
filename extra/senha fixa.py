senha = 2002
acesso = int(input())

while acesso != senha:
    print("Senha invalida")
    acesso = int(input())
    
    if acesso == senha:
        print("Acesso permitido")

   