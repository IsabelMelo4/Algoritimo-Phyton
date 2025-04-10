n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10
print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame")
    nota = float(input())
    print("Nota do exame {}".format(nota))
    media2= (media + nota) / 2

    if media2 > 5.0:
        print("Aluno aprovado.")
        media3 = (n1 + n2 + n3 + n4 + nota) // 5
        print("Media final: {:.1f}".format(media3))

    else:
        print("Aluno reprovado.")




