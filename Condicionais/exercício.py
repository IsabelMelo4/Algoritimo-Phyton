n1 = float(input())
n2 = float(input())
n3 = float(input())

delta = n2 ** 2 -4 * n1 * n3


if delta == 0 or delta < 0:
    print("impossível calcular")
else:
    x1=(-n2 + delta ** 0.5) / 2*n1 
    x2=(-n2 - delta ** 0.5) / 2*n1

print("x1 = {:.5f}".format(x1))
print("x2 = {:.5f}".format(x2))
