testes = int(input())
termina = 0

for i in range(testes):
    a, b = map(str, input().split())

    termina = a.endswith(b) 

    if termina == True:
        print("encaixa")
    else:
        print("nao encaixa")
    

   


