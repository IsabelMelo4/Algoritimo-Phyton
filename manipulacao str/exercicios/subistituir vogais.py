texto = input()

vogais = "aeiouAEIOU"
novaPalavra = ""

for letra in texto:
    if letra in vogais:
        novaPalavra += "x"
    else:
        novaPalavra += letra
print(novaPalavra)

