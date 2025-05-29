testes = int(input())


for i in range(testes):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    contador = 0
    while pa <= pb:
   
      pa = int(pa + (pa * g1 / 100))
      pb = int(pb + (pb * g2 / 100))
      contador += 1

    if contador > 100:
       break

    print("Mais de 1 seculo" if contador > 100 else "{} anos.".format(contador))