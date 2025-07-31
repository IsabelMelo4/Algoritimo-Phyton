texto = input()
palavra = input()

posicao = texto.find(palavra)

if posicao != -1:
    print(posicao)
else:
    print(" ")