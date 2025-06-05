nota1 = float(input())
nota2 = float(input())
media = 0
  
while nota1 > 10 or nota2 > 10 and nota2 < 0 or nota1 < 0:
    print("nota invalida")

    if nota1 < 0. or nota1 > 10.:
        nota1 = float(input())

    if nota2 < 0. or nota2 > 10.:
         nota2 = float(input())

media = (nota1 + nota2) / 2
print("media = {:.2f}".format(media))  