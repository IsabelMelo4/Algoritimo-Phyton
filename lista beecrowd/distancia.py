eixoX1, eixoY1 = input().split()
eixoX2, eixoY2 = input().split()

eixoX1 = float(eixoX1)
eixoY1 = float(eixoY1)

eixoX2 = float(eixoX2)
eixoY2 = float(eixoY2)

distancia = (eixoX2 - eixoX1) ** 2 + (eixoY2 -  eixoY1) ** 2 **0.5

print("{:.4f}".format(distancia))

