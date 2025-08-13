def soma_m(media):
    return sum(media)

media_alunos = []
media_anual = []

total_alunos = int(input())


for i in range(total_alunos):
    n1,n2,n3,n4 = map(float, input().split())
    calcular_media = (n1 + n2 +n3 + n4) //4
    media_alunos.append(calcular_media)

r_f = soma_m(media_alunos) // len(media_alunos)

print(media_alunos)
print(r_f)

