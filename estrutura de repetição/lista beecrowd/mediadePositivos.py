valor = 0
soma = 0


for c in range (0, 6):
    num = float(input())
    if num > 0:
        valor += 1
        soma = soma + num
       

media = soma / valor

print("{} valores positivos".format(valor))
print("{:.1f}".format(media))