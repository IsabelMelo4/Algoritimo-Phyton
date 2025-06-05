repetir = 0
media = 0
soma = 0
contador = 0

while repetir != 2 :

    nota = float(input())
    repetir = 0

    if nota < 0 or nota > 10:
        print("nota invalida")

    else:
        soma += nota
        contador += 1

    if(contador == 2):
        contador = 0
        media = soma/2
        soma = 0
        print("media = {:.2f}".format(media))

        while repetir != 1 and repetir !=2:
            print("novo calculo (1-sim 2-nao)")
            repetir = int(input())