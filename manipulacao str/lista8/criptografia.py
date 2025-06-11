testes = int(input())

for n in range(testes):
    nome = (input())
    novaPalavra = ""

    for letra in nome:
        if letra.isalpha():
            novoCaractere = chr((ord(letra) + 3))
            novaPalavra += novoCaractere
        else:
            novaPalavra += letra

    novaPalavra = novaPalavra[::-1]
    metade = len(novaPalavra)//2

    novaPalavra_final = ""

    for k in range(len(novaPalavra)):
        letra = novaPalavra[k]

        if k >= metade:
            novoCaractere = chr((ord(letra) - 1))
            novaPalavra_final += novoCaractere
        else:
            novaPalavra_final += letra

    print(novaPalavra_final)
    
