testes = int(input())


for n in range(testes):
    texto = input()
    textoC = ""
    metadeE = texto[:len(texto)//2]
    metadeD = texto[len(texto)//2:]

    textoC += metadeE[::-1]
    textoC += metadeD[::-1]

    print(textoC)