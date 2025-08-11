def fatorial(fat, pos, pulo):
    if pos <= 0:
        return 1
    
    return fat * fatorial(fat - pulo, pos - pulo, pulo)


teste=int(input())

for _ in range(teste):

    n = input()
    quantidade = n.count("!")  #count para contar quantos ! tem
    numero_fatorial = int(n.rstrip("!")) #lstrip pra tirar os ! e pegar o numero
    posicao = numero_fatorial
    print(fatorial(numero_fatorial, posicao, quantidade))

