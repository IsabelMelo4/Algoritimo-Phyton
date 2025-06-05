testes = int(input())
cont = 1 

for n in range(testes):
    nome = str(input())
    novaPalavra = ""

    for i in range(len(nome)):
        letra = nome[i]
        if letra.isalpha():
            novoCaractere = chr((ord(letra) + 3))
            novaPalavra += novoCaractere
        else:
            novaPalavra += letra

    novaPalavra = novaPalavra[::-1]
    metade = len(novaPalavra)//2

    novaPalavra_final = ""

    for k in range(metade, len(novaPalavra)):
        letra = novaPalavra[i]

        if i >= metade:
            novoCaractere = chr((ord(letra) - 1))
            novaPalavra_final += novoCaractere
        else:
            novaPalavra_final += letra

print(novaPalavra_final)
    
