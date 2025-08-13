# fazer um progama que guarde a media e o nome e a situação do aluno 

media = []
aluno = {}

aluno["nome"] = str(input("Nome do aluno:"))

aluno["media"] = float(input("media do aluno:"))

if aluno["media"] < 7:
    aluno["situação"] = "reprovado"
else:
    aluno["situação"] = "Aprovado"

media.append(aluno)
for e in media:
 print(e)
