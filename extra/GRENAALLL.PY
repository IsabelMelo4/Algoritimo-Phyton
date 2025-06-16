
empates = 0
totalJogos = 0
inter = 0
gremio = 0

while True:

    totalInter, totalGremio = map(int, input().split())

    if totalGremio > totalInter:
           gremio += 1
    elif totalInter > totalGremio:
           inter += 1
    elif totalInter == totalGremio:
           empates += 1
    totalJogos+=1
    print("Novo grenal (1-sim 2-nao)")

    novo_grenal = int(input())
    if novo_grenal!= 1:
          break

print("{} grenais".format(totalJogos))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empates))

if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
