codigo, quantidade = map(int, input().split())

if codigo == 1:
    codigo = float(4.00)
elif codigo == 2:
   codigo = float(4.50)
elif codigo == 3:
   codigo = float(5.00)
elif codigo == 4:
    codigo = float(2.00)
elif codigo == 5:
    codigo = float(1.50)

total = float(codigo * quantidade)

print("Total: R$ {:.2f}".format(total))
